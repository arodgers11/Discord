import discord
from discord.ext import commands
import pandas as pd
import requests

teams=[
'/overwatch/Atlanta_Reign',
'/overwatch/Boston_Uprising',
'/overwatch/Chengdu_Hunters',
'/overwatch/Dallas_Fuel',
'/overwatch/Florida_Mayhem',
'/overwatch/Guangzhou_Charge',
'/overwatch/Hangzhou_Spark',
'/overwatch/Houston_Outlaws',
'/overwatch/London_Spitfire',
'/overwatch/Los_Angeles_Gladiators',
'/overwatch/Los_Angeles_Valiant',
'/overwatch/New_York_Excelsior',
'/overwatch/Paris_Eternal',
'/overwatch/Philadelphia_Fusion',
'/overwatch/San_Francisco_Shock',
'/overwatch/Seoul_Dynasty',
'/overwatch/Shanghai_Dragons',
'/overwatch/Toronto_Defiant',
'/overwatch/Vancouver_Titans',
'/overwatch/Washington_Justice'
]

class OWL_wiki(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('OWL_wiki Loaded')
        
    @commands.command(aliases=['get_team','roster'])
    async def team(self,ctx,*,team):
        """Prints the active roster for an OWL team. Accepts partial names."""
        url='https://liquipedia.net'
        t='No Team Found'
        for i in teams:
            if team.upper() in i.upper():
                t=i
                break
        tables=pd.read_html(requests.get(url+t).content)
        table=None
        for i in range(0,len(teams)):
            try:
                table=tables[i]['Active Squad'][['ID','Role']].sort_values(['Role', 'ID'], ascending=[1, 0])
            except:
                None
                                
        if table is None:
            await ctx.send("Team Not Found")
            return
                
        s=['']*len(table)
        for i in range(0,len(table)):
            s[i]=table['ID'][i]+' '+'.'*(25-len(table['ID'][i])-len(table['Role'][i]))+' '+table['Role'][i]
        TEAM_NAME='**'+t[11:len(t)].replace('_',' ')+'**'
        table[TEAM_NAME]=s
        df=table[[TEAM_NAME]]
        df.index=['']*len(df)
        await ctx.send(df)

    @commands.command(aliases=['liquipedia','liq'])
    async def wiki(self,ctx,*team):
        """Gets the Liquipedia link for an OWL team.
        Can also use .teams , or .players to get the teams or players links, respectively"""
        url='<https://liquipedia.net'
        if len(team)==0:
            await ctx.send(url+'/overwatch/Overwatch_League>')
            return
        if team=='players':
            await ctx.send(url+'/overwatch/Players>')
            return
        if team=='teams':
            await ctx.send(url+'/overwatch/Portal:Teams/Overwatch_League>')
            return
        for i in teams:
            if team[0].upper() in i[11:].upper():
                t=i
                break
            else:
                t='No Team Found'
        if t!='No Team Found':
            await ctx.send(url+t+'>')
        else:
            print('NO TEAM FOUND')
            await ctx.send('No Team Found')

def setup(bot):
    bot.add_cog(OWL_wiki(bot))
