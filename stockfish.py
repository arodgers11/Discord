import discord
from discord.ext import commands

allowed_channels=['stockfish-war-room','bots']

client=commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('READY')

client=commands.Bot(command_prefix='.')

@client.command(aliases=['c'])
async def clear(ctx,amount=20):
    await ctx.channel.purge(limit=amount)

@client.event
async def on_ready():
    print('READY')

client.load_extension('cogs.OWL_wiki')
client.load_extension('cogs.Music')
        
client.run('NzE4MDIyNzE3ODUyNDgzNjQ2.Xti0zw.owv5tLeBNNXsZkK3gZ1uXVjtqx0',
           bot=True,
           reconnect=True)