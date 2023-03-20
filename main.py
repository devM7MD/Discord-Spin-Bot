import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all(), )
array = []

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command(name="items_list")
async def items_list(ctx):
    # Send message to discord with the list of items
    await ctx.send(f"**Items in the list:**\n**` {', '.join(array)} `**")

@bot.command(name="add_item")
async def add_item(ctx, *, item):
    # Make sure the item not already added
    if item in array:
        await ctx.send("**Item already added :x:**")
    elif item not in array:
        # Add a new item to the list
        array.append(str(item))
        # Send message to discord 👍
        await ctx.send(f"**`{item}` has been added to the list :white_check_mark:**")

@bot.command(name="delete_item")
async def delete_item(ctx, *, item):
    # Make sure the item not already added
    if item in array:
        # Delete the item from the list
        array.remove(item)
        # Send message to discord 👎
        await ctx.send(f"**`{item}` has been removed from the list :white_check_mark:**")
    elif item not in array:
        await ctx.send(f"**the `{item}` item not found in the data :x:**")

@bot.command(name="spin")
async def spin(ctx):
    # Make sure the list have any items
    if array == [] :
        await ctx.send("**No items in the list :x:**")
    else:
        # Get a random item from the list
        item = random.choice(array)
        # Send message to discord with the item
        await ctx.send(f"**Congratulations {ctx.author.mention} you are win `{item}` :tada: **")

bot.run("your-token-here")
