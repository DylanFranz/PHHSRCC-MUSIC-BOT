import discord
from discord.ext import commands
import youtube_dl
import time
queue = []

class music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def disconnect(self,ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def clearQueue(self,ctx):
        queue.clear()
        await ctx.send('Queue cleared!')

    @commands.command()
    async def remove(self,ctx,num):
        queue.pop(int(num) - 1)
        await ctx.send('Song has been removed!')

    @commands.command()
    async def listQueue(self,ctx):
        await ctx.send('fetching queue info...')
        queueLength = len(queue)
        i = 1
        if queueLength > 0:
          while queueLength > 0:
              YDL_OPTIONS = {'format':'bestaudio'}
              with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(queue[i - 1], download=False)
                name = info['title']
                await ctx.send(str(i) + '. ' + name)
              i += 1
              queueLength -= 1
              continue
        else:
          await ctx.send('Queue is empty!')


    @commands.command()
    async def queuePlay(self,ctx):
      if ctx.author.voice is None:
            await ctx.send("YOU ARENT DEDICATED ENOUGH TO BE IN VCCCC")
      voice_channel = ctx.author.voice.channel
      if ctx.voice_client is None:
          await voice_channel.connect()
      else:
          await ctx.voice_client.move_to(voice_channel)
      while len(queue) > 0:
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format':'bestaudio'}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(queue.pop(0), download=False)
            url2 = info['formats'][0]['url']
            length = info['duration']
            name = info['title']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)
            await ctx.send('Now playing: ' + name)
            time.sleep(length)
            continue

    @commands.command()
    async def play(self,ctx,url):
      if ctx.author.voice is None:
          await ctx.send("YOU ARENT DEDICATED ENOUGH TO BE IN VCCCC")
      voice_channel = ctx.author.voice.channel
      if ctx.voice_client is None:
          await voice_channel.connect()
      else:
          await ctx.voice_client.move_to(voice_channel)
      ctx.voice_client.stop()
      FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
      YDL_OPTIONS = {'format':'bestaudio'}
      vc = ctx.voice_client

      with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
          info = ydl.extract_info(url, download=False)
          url2 = info['formats'][0]['url']
          name = info['title']
          source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
          vc.play(source)
          await ctx.send('Now playing: ' + name)

    @commands.command()
    async def pause(self,ctx):
        await ctx.send('paused!')
        await ctx.voice_client.pause()

    @commands.command()
    async def resume(self,ctx):
        await ctx.send('resumed!')
        await ctx.voice_client.resume()

    @commands.command()
    async def queue(self,ctx,url):
        await ctx.send("PLEASE NOTE: you cannot pause or stop a queue **OR** use any other command once started\nuse -queuePlay to play it")
        queue.append(url)

    


    
def setup(client):
    client.add_cog(music(client))