import discord
from discord.ext import commands

class stalker(commands.Cog):    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Stalker Loaded')

#@client.event
#async def on_member_update(before, after):
    #if before.id=""
        #if before.status != after.status:  # to only run on status

    @commands.command()
    async def off(self,ctx):
        #async for user in ctx.guild.fetch_members(limit=None):
        for user in ctx.guild.members:
            #print(user.status)
            if user.status != discord.Status.offline:
                print(user.name, " ",user.id)

def setup(bot):
    bot.add_cog(stalker(bot))
