import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = "!")
@client.event
async def on_ready():
    print("The bot is ready")

@client.command(aliases=['hey', 'hi'])
async def hello(ctx):
    await ctx.send("Hello :wave: , I am Nitro. How's it going? ")

client.run(os.environ("token"))