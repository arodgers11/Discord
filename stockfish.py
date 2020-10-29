import discord
from discord.ext import commands
import asyncio
import os

client=commands.Bot(command_prefix='.')

TOKEN=os.environ['BOT_TOKEN']

@client.event
async def on_ready():
    print('READY')

client=commands.Bot(command_prefix='.')

@client.command(aliases=['c'])
async def clear(ctx,amount=20):
    await ctx.channel.purge(limit=amount)
    
@client.event
async def on_voice_state_update(member, before, after):
    if after.channel is not None and not member.bot:
        if not before.self_deaf and not before.self_mute and not after.self_deaf and not after.self_mute:
            if after.channel.name in ['Lt. Deen\'s Alpha Squad','OW Bravo Squad','The War Room']:
                await asyncio.sleep(1)
                if not client.voice_clients:
                    vc = await after.channel.connect()
                else:
                    vc = client.voice_clients[0]
                print(member.display_name)
                if vc and not vc.is_playing():
                    vc.play(discord.FFmpegPCMAudio(f'./cogs/sounds/walk-on/{member.display_name}.mp3'), after=lambda e: print('done', e))
                    while vc.is_playing():
                        await asyncio.sleep(1)
                await vc.disconnect()

client.load_extension('cogs.Music')
client.load_extension('OWL_wiki')

@client.event
async def on_ready():
    print('READY')
        
client.run(TOKEN,bot=True,reconnect=True)