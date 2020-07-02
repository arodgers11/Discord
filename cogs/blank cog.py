import discord
from discord.ext import commands
import OWL

class OWL_stats(commands.Cog):    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('OWL_stats Loaded')
		
		
def setup(bot):
    bot.add_cog(OWL_stats(bot))
