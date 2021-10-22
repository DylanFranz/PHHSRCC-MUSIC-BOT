import discord
from discord.ext import commands
from morse3 import Morse as m


class utility(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def mcEncrypt(self,ctx,text):
        await ctx.send('"'+ m(text).stringToMorse()+ '"')

    @commands.command()
    async def mcDecrypt(self,ctx,text):
        await ctx.send(m(text).morseToString())

def setup(client):
    client.add_cog(utility(client))