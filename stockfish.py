import discord
from discord.ext import commands
#from boto.s3.connection import S3Connection
#import os
TOKEN='NzE4MDIyNzE3ODUyNDgzNjQ2.Xv1bYw.kURsxX7RIigUR-egXyYbCofi9o8'

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
