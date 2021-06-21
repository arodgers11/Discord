import discord
from discord.ext import commands
import asyncio
import os

intents = discord.Intents().all()
client = commands.Bot(command_prefix='.', intents=intents)

TOKEN=os.environ['BOT_TOKEN']

@client.event
async def on_ready():
    print('READY')

@client.command(aliases=['c'])
async def clear(ctx,amount=20):
    await ctx.channel.purge(limit=amount)

client.load_extension('cogs.Music')
#client.load_extension('cogs.OWL_wiki')
client.load_extension('cogs.stalker')

@client.event
async def on_ready():
    print('READY')
        
client.run(TOKEN,bot=True,reconnect=True)
