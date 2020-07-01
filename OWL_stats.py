import discord
from discord.ext import commands
import OWL
import pandas as pd

class OWL_stats(commands.Cog):    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('OWL_stats Loaded')

    @client.event
    async def on_ready():
    await client.change_presence(status=discord.Status.online,activity=discord.Activity(type=discord.ActivityType.watching,name='Overwatch League'))
    print('Ready')

    @client.command(aliases=['map'])
    async def OWLmap(ctx,map,team,season):
        if not isinstance(ctx.channel,discord.DMChannel):
            return
        else:
            await ctx.send(OWL.map_stats(map,team,season=0))
            print(OWL.map_stats(map,team,season))

    @client.command(aliases=['phs'])
    async def rank(ctx,player,map,hero,season,stage):
        if not isinstance(ctx.channel,discord.DMChannel):
            return
        else:
            [p,m,h,results]=OWL.player_hero_stats(player,map,hero,season,stage)
            print(p,m,h,'\n')
            stats=results.groupby('stat_name')['stat_amount'].sum()
            print(stats.round(0))


def setup(bot):
    bot.add_cog(OWL_wiki(bot))
