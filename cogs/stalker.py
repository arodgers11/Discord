import discord
from discord.ext import commands

class stalker(commands.Cog):    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Stalker Loaded')
                
    @commands.command()
    async def offline_users(self,ctx):
        #async for user in ctx.guild.fetch_members(limit=None):
        for user in ctx.guild.members:
            #print(user.status)
            if user.status = discord.Status.offline:
                print(user.name, " ",user.id)

def setup(bot):
    bot.add_cog(stalker(bot))
