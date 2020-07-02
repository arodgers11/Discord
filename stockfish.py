import discord
import os
from discord.ext import commands
print(os.environ['BOT_TOKEN'])
TOKEN='asdf'
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
client.load_extension('cogs.Music')

@client.event
async def on_ready():
    print('READY')
        
client.run(TOKEN,
           bot=True,
           reconnect=True)
