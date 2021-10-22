import discord
from discord.ext import commands
import music
import os
import cubing
import utility
from keep_alive import keep_alive

CLIENT_KEY = os.environ['CLIENT_KEY']

cogs = [music, cubing, utility]

client = commands.Bot(command_prefix='-', intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

keep_alive()

client.run(CLIENT_KEY)

