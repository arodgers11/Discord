import discord
from discord.ext import commands
import youtube_dl
import asyncio
import time

spam_lock=time.time()

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': False,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}

ffmpeg_options = {
    'options': '-vn'
    }

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

spam_lock=time.time()

def play_file(ctx,file_path):
    global spam_lock
    if time.time()-spam_lock<10:
        spam_lock=time.time()
        await ctx.send("FOR FUCK'S SAKE STOP SPAMMING COMMANDS!!")
        await ctx.send(":face_with_symbols_over_mouth:")
    else:
        spam_lock=time.time()
        ctx.voice_client.play(discord.FFmpegPCMAudio(source=file_path))

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

class Music(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
    async def player(self,ctx):
        global spam_lock
        if time.time()-spam_lock<10:
            spam_lock=time.time()
            return
        else:
            while  ctx.voice_client:
                while ctx.voice_client.is_playing() or ctx.voice_client.is_paused():
                    await asyncio.sleep(1)
                    if not ctx.voice_client:
                        break
                if ctx.voice_client:
                    await ctx.voice_client.disconnect()
                else:
                    return

    @commands.Cog.listener()
    async def on_ready(self):
        print('Music Loaded')

    @commands.command()
    async def play(self, ctx, url):
        """Plays music from a YouTube url"""
        url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        player = await YTDLSource.from_url(url,loop=self.bot.loop,stream=True)
        ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

    @commands.command(aliases=['p'])
    async def pause(self,ctx):
        paused = ctx.voice_client.is_paused()
        if not paused:
            ctx.voice_client.pause()
        else:
            return

    @commands.command(aliases=['r'])
    async def resume(self,ctx):
        paused = ctx.voice_client.is_paused()
        if paused:
            ctx.voice_client.resume()
        else:
            return

    @commands.command(aliases=['stop','stfu'])
    async def leave(self, ctx):
        """Stops music and disconnects the bot from voice"""
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
        else:
            return

################################################################

    @commands.command()
    async def alert(self,ctx):
        play_file(ctx,'./cogs/sounds/alert.mp3')
        await self.player(ctx)
            
    @commands.command()
    async def again(self,ctx):
        play_file(ctx,'./cogs/sounds/again.mp3')
        await self.player(ctx)
            
    @commands.command()
    async def bill(self,ctx):
        play_file(ctx,'./cogs/sounds/bill.mp3')
        await self.player(ctx)
                
    @commands.command()
    async def boi(self,ctx):
        play_file(ctx,'./cogs/sounds/boi.mp3')
        await self.player(ctx)
                
    @commands.command()
    async def boo(self,ctx):
        play_file(ctx,'./cogs/sounds/boo.mp3')
        await self.player(ctx)
                
    @commands.command()
    async def bourne(self,ctx):
        play_file(ctx,'./cogs/sounds/bourne.mp3')
        await self.player(ctx)
            
    @commands.command()
    async def bruh(self,ctx):
        play_file(ctx,'./cogs/sounds/bruh.mp3')
        await self.player(ctx)
                
    @commands.command()
    async def cena(self,ctx):
        play_file(ctx,'./cogs/sounds/cena.mp3')
        await self.player(ctx)
                
    @commands.command()
    async def crickets(self,ctx):
        play_file(ctx,'./cogs/sounds/crickets.mp3')
        await self.player(ctx)
                
    @commands.command()
    async def damage(self,ctx):
        play_file(ctx,'./cogs/sounds/damage.mp3')
        await self.player(ctx)
                
    @commands.command()
    async def damn(self,ctx):
        play_file(ctx,'./cogs/sounds/damn.mp3')
        await self.player(ctx)
                
    @commands.command()
    async def disbelief(self,ctx):
        play_file(ctx,'./cogs/sounds/disbelief.mp3')
        await self.player(ctx)
                
    @commands.command()
    async def dreams(self,ctx):
        play_file(ctx,'./cogs/sounds/dreams.mp3')
        await self.player(ctx)
                
    @commands.command()
    async def horns(self,ctx):
        play_file(ctx,'./cogs/sounds/horns.mp3')
        await self.player(ctx)
            
    @commands.command()
    async def lbj(self,ctx):
        play_file(ctx,'./cogs/sounds/lbj.mp3')
        await self.player(ctx)
            
    @commands.command()
    async def leedle(self,ctx):
        play_file(ctx,'./cogs/sounds/leedle.mp3')
        await self.player(ctx)
            
    @commands.command()
    async def leeroy(self,ctx):
        play_file(ctx,'./cogs/sounds/leeroy.mp3')
        await self.player(ctx)
            
    @commands.command()
    async def loser(self,ctx):
        play_file(ctx,'./cogs/sounds/loser.mp3')
        await self.player(ctx)
            
    @commands.command()
    async def mission(self,ctx):
        play_file(ctx,'./cogs/sounds/mission.mp3')
        await self.player(ctx)
            
    @commands.command()
    async def nope(self,ctx):
        play_file(ctx,'./cogs/sounds/nope.mp3')
        await self.player(ctx)
            
    @commands.command()
    async def pain(self,ctx):
        play_file(ctx,'./cogs/sounds/pain.mp3')
        await self.player(ctx)
            
    @commands.command()
    async def peepee(self,ctx):
        play_file(ctx,'./cogs/sounds/peepee.mp3')
        await self.player(ctx)
            
    @commands.command()
    async def over9000(self,ctx):
        play_file(ctx,'./cogs/sounds/over9000.mp3')
        await self.player(ctx)
        
    @commands.command()
    async def ph(self,ctx):
        play_file(ctx,'./cogs/sounds/ph.mp3')
        await self.player(ctx)
        
    @commands.command()
    async def peepee(self,ctx):
        play_file(ctx,'./cogs/sounds/peepee.mp3')
        await self.player(ctx)
            
    @commands.command()
    async def scat(self,ctx):
        play_file(ctx,'./cogs/sounds/scat.mp3')
        await self.player(ctx)
            
    @commands.command()
    async def shia(self,ctx):
        play_file(ctx,'./cogs/sounds/shia.mp3')
        await self.player(ctx)
            
    @commands.command()
    async def simp(self,ctx):
        play_file(ctx,'./cogs/sounds/simp.mp3')
        await self.player(ctx)
            
    @commands.command()
    async def skinny(self,ctx):
        play_file(ctx,'./cogs/sounds/skinny.mp3')
        await self.player(ctx)
            
    @commands.command()
    async def suit(self,ctx):
        play_file(ctx,'./cogs/sounds/suit.mp3')
        await self.player(ctx)
            
    @commands.command()
    async def svu(self,ctx):
        play_file(ctx,'./cogs/sounds/svu.mp3')
        await self.player(ctx)
            
    @commands.command()
    async def tralala(self,ctx):
        play_file(ctx,'./cogs/sounds/tralala.mp3')
        await self.player(ctx)
        
    @commands.command()
    async def trombone(self,ctx):
        play_file(ctx,'./cogs/sounds/trombone.mp3')
        await self.player(ctx)
            
    @commands.command()
    async def violin(self,ctx):
        play_file(ctx,'./cogs/sounds/violin.mp3')
        await self.player(ctx)
            
    @commands.command()
    async def wilhelm(self,ctx):
        play_file(ctx,'./cogs/sounds/wilhelm.mp3')
        await self.player(ctx)
            
    @commands.command()
    async def yakuza(self,ctx):
        play_file(ctx,'./cogs/sounds/yakuza.mp3')
        await self.player(ctx)
        
    @commands.command()
    async def dallas(self,ctx):
        play_file(ctx,'./cogs/sounds/rialto.mp3')
        await self.player(ctx)
        rialto='https://www.youtube.com/watch?v=z4hM5GG6QCg'
                                
    @commands.command(aliases=['cock'])
    async def penis(self, ctx):
        nice_cock='https://www.youtube.com/watch?v=JdCq2i1dA6w'
        player = await YTDLSource.from_url(nice_cock,loop=self.bot.loop,stream=True)
        ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
        await self.player(ctx)

    @commands.command()
    async def hello(self,ctx,*s):
        """Says hello"""
        if len(s)>0:
            if s[0].lower()=='there':
                if ctx.voice_client is None:
                    if ctx.author.voice:
                        await ctx.author.voice.channel.connect()
                        player = await YTDLSource.from_url('https://www.youtube.com/watch?v=rEq1Z0bjdwc',loop=self.bot.loop,stream=True)
                        ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
                        await self.player(ctx)
                    else:
                        await ctx.send("General Kenobi")
        if len(s)==0:
            await ctx.send('Hello **{}**!!'.format(ctx.author.name))
            
    @again.before_invoke
    @alert.before_invoke
    @bill.before_invoke
    @boi.before_invoke
    @boo.before_invoke
    @bourne.before_invoke
    @bruh.before_invoke
    @cena.before_invoke
    @crickets.before_invoke
    @damage.before_invoke
    @damn.before_invoke
    @disbelief.before_invoke
    @dreams.before_invoke
    @horns.before_invoke
    @lbj.before_invoke
    @leedle.before_invoke
    @leeroy.before_invoke
    @loser.before_invoke
    @mission.before_invoke
    @nope.before_invoke
    @over9000.before_invoke
    @pain.before_invoke
    @peepee.before_invoke
    @ph.before_invoke
    @scat.before_invoke
    @shia.before_invoke
    @simp.before_invoke
    @skinny.before_invoke
    @suit.before_invoke
    @svu.before_invoke
    @tralala.before_invoke
    @trombone.before_invoke
    @violin.before_invoke
    @wilhelm.before_invoke
    @yakuza.before_invoke
    
    @dallas.before_invoke
    @penis.before_invoke
    
    async def ensure_voice(self, ctx):
        global spam_lock
        if time.time()-spam_lock>=10:
            spam_lock=time.time()
            if ctx.voice_client is None:
                if ctx.author.voice:
                    await ctx.author.voice.channel.connect()
                    self.voice_channel=ctx.author.voice.channel
                else:
                    await ctx.send("You are not connected to a voice channel.")
                    raise commands.CommandError("Author not connected to a voice channel.")
            elif ctx.voice_client.is_playing():
                ctx.voice_client.stop()
            
def setup(bot):
    bot.add_cog(Music(bot))