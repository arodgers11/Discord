import discord
from discord.ext import commands

class stalker(commands.Cog):    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Stalker Loaded')

@client.event
async def on_member_update(before, after):
    if before.name='andyarchy':
        if before.status != after.status:
            if after.status=="offline":
                client.users.fetch('215957034820960256', false).then((user) => {
 user.send('andyarchy is online);
});
                
    @commands.command()
    async def offline_users(self,ctx):
        #async for user in ctx.guild.fetch_members(limit=None):
        for user in ctx.guild.members:
            #print(user.status)
            if user.status = discord.Status.offline:
                print(user.name, " ",user.id)

def setup(bot):
    bot.add_cog(stalker(bot))
