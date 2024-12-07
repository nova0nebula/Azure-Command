# Importing
import discord
from discord.ext import commands

# Replace 'token_here' with your Discord bot token
TOKEN = 'token_here'

# Define bot prefix
bot = commands.Bot(command_prefix='!')

# Event handler for when the bot is ready
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# Command handler for the 'ping' command
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Run the bot
bot.run(TOKEN)