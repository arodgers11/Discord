import discord
from discord.ext import commands
import youtube_dl
import asyncio
import time

allowed_channels=['stockfish-war-room','bots']

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
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

players={}

def play_file(ctx,file_path):
        ctx.voice_client.play(discord.FFmpegPCMAudio(executable='./FFmpeg/bin/ffmpeg.exe', source=file_path))
    
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
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Music Loaded')

    @commands.command()
    async def play(self, ctx, url):
        """Plays music from a YouTube url"""
        url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        player = await YTDLSource.from_url(url,loop=self.bot.loop,stream=False)
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

    @commands.command(aliases=['stop','l'])
    async def leave(self, ctx):
        """Stops music and disconnects the bot from voice"""
        await ctx.voice_client.disconnect()
        
    @commands.command(aliases=['fuel','burnblue','Dallas','Fuel','BurnBlue'])
    async def dallas(self,ctx):
        if not str(ctx.channel) in allowed_channels:
            return
        else:
            play_file(ctx,'./cogs/sounds/rialto.mp3')
            rialto='https://www.youtube.com/watch?v=z4hM5GG6QCg'

    @commands.command(aliases=['b'])
    async def bruh(self,ctx):
        if not str(ctx.channel) in allowed_channels:
            return
        else:
            play_file(ctx,'./cogs/sounds/bruh.mp3')
            time.sleep(1)
            await ctx.voice_client.disconnect()
                                
    @commands.command(aliases=['cock'])
    async def penis(self, ctx):
        nice_cock='https://www.youtube.com/watch?v=JdCq2i1dA6w'
        player = await YTDLSource.from_url(nice_cock,loop=self.bot.loop,stream=False)
        ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
        time.sleep(26)
        await ctx.voice_client.disconnect()

    @commands.command()
    async def hello(self,ctx,*s):
        """Says hello, obviously"""
        if len(s)>0:
            if s[0].lower()=='there':
                if ctx.voice_client is None:
                    if ctx.author.voice:
                        await ctx.author.voice.channel.connect()
                        player = await YTDLSource.from_url('https://www.youtube.com/watch?v=rEq1Z0bjdwc',loop=self.bot.loop,stream=False)
                        ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
                        time.sleep(14)
                        await ctx.voice_client.disconnect()
                    else:
                        await ctx.send("You are not connected to a voice channel.")
                        raise commands.CommandError("Author not connected to a voice channel.")
        if len(s)==0:
            await ctx.send('Hello **{}**!!'.format(ctx.author.name))
			
    @commands.command()
    async def boi(self,ctx):
        """YEAH BOIIIIIII"""
        yeah_boi='https://www.youtube.com/watch?v=5aopMm7UGYA'
        player = await YTDLSource.from_url(yeah_boi,loop=self.bot.loop,stream=False)
        ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
        time.sleep(30)
        await ctx.voice_client.disconnect()
			
    @play.before_invoke
    @penis.before_invoke
    @dallas.before_invoke
    @bruh.before_invoke
    @pause.before_invoke
    @resume.before_invoke
    @boi.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()
            
def setup(bot):
    bot.add_cog(Music(bot))
