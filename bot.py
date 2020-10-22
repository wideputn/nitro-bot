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

@client.command(aliases=['c'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)

@client.command(aliases=['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason = "Not provided"):
    await member.kick(reason=reason)
    serverName = ctx.message.guild.name
    await member.send("You have been kicked from the " + serverName)
    await member.send("Reason: " + reason)
    await ctx.send(member.name + " has been kicked from the " + serverName)

@client.command(aliases=['b'])
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = "Not provided"):
    await member.ban(reason=reason)
    serverName = ctx.message.guild.name
    await member.send("You have been banned from the " + serverName)
    await member.send("Reason: " + reason)
    await ctx.send(member.name + " has been banned from the " + serverName)

client.run(os.environ["token"])