import discord
from discord.ext import commands
from pyTwistyScrambler import scrambler333, scrambler222, scrambler444,\
	megaminxScrambler, squareOneScrambler, ftoScrambler, rexScrambler

class cubing(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def scramble3(self,ctx):
        await ctx.send(scrambler333.get_WCA_scramble())

    @commands.command()
    async def scramble2(self,ctx):
        await ctx.send(scrambler222.get_WCA_scramble())

    @commands.command()
    async def scramble4(self,ctx):
        await ctx.send(scrambler444.get_WCA_scramble())

    @commands.command()
    async def scramblesq1(self,ctx):
        await ctx.send(squareOneScrambler.get_WCA_scramble())

    @commands.command()
    async def scramblemega(self,ctx):
        await ctx.send(megaminxScrambler.get_WCA_scramble())

def setup(client):
    client.add_cog(cubing(client))