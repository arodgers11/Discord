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

@client.event
async def on_member_update(before, after):
    if before.name=='andyarchy' or before.name=='arodgers':
        if before.status != after.status or before.activity != after.activity:
            if after.status != "offline" and after.status != 'do_not_disturb':
                user = client.get_user(215957034820960256)
                print(after.activity)
                print(after.status)
                await user.send( after.name + " is online")

#client.load_extension('cogs.Music')
#client.load_extension('cogs.OWL_wiki')
client.load_extension('cogs.stalker')

@client.event
async def on_ready():
    print('READY')
        
client.run(TOKEN,bot=True,reconnect=True)
