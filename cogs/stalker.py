import discord
from discord.ext import commands
import OWL

class stalker(commands.Cog):    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Stalker Loaded')

#@client.event
#async def on_member_update(before, after):
    #if before.status != after.status:  # to only run on status
        #if

    @commands.command()
    async def off(self,ctx):
        for user in ctx.guild.members:
            #print(user.status)
            print(user.status)

def setup(bot):
    bot.add_cog(stalker(bot))
