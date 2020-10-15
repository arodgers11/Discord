import discord
from discord.ext import commands
import os

TOKEN='NzE4MDIyNzE3ODUyNDgzNjQ2.XwVLCQ.hzuLdgeKfMdj-aP8yZohFyvHS0Q'

allowed_channels=['stockfish-war-room','bots']

client=commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('READY')

client=commands.Bot(command_prefix='.')

@client.command(aliases=['c'])
async def clear(ctx,amount=20):
    await ctx.channel.purge(limit=amount)

client.load_extension('cogs.OWL_wiki')

@client.command()
async def load(ctx,ext):
    if ext.lower()=='music':
        extension='Music'
    # if ext.lower()=='wiki':
        # extension='OWL_wiki'
    # if ext.lower()=='stats':
        # extension='OWL_stats'
    client.load_extension(f'cogs.{extension}')
    print(f'{extension} Loaded')

@client.command()
async def unload(ctx,ext):
    if ext.lower()=='music':
        extension='Music'
    if ext.lower()=='wiki':
        extension='OWL_wiki'
    if ext.lower()=='stats':
        extension='OWL_stats'
    client.unload_extension(f'cogs.{extension}')
    print(f'{extension} Unloaded')

@client.event
async def on_ready():
    print('READY')
        
client.run(TOKEN,bot=True,reconnect=True)