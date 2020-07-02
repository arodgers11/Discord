import discord
from discord.ext import commands
import OWL

class OWL_stats(commands.Cog):    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('OWL_stats Loaded')
		
	@commands.command(aliases=['stats','per10'])
	async def statsper10.(self,ctx,player,*hero,*map):
		"""Prints stats per 10 for a player"""
		"""Accepts additional options (hero("ALL"),map)"""
		if hero.lower()=='all':
			hero='All Heroes'
		if not hero:
			hero='All Heroes'
		await ctx.send(OWL.hero_stats_per_10(player,hero,map,2020,1))
		
def setup(bot):
    bot.add_cog(OWL_stats(bot))
