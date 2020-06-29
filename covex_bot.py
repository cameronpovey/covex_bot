import discord
import os
import time
import random
import sys
import giphy_client
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle
from giphy_client.rest import ApiException

client = commands.Bot(command_prefix= "-")

status = cycle(['-help for help.', 'discord.gg/vgMqZ7A <- Covex Bot Server'])
def clear():
    os.system( 'clear' ) #for windows change to 'cls', for mac and linux change to 'clear'

#on startup:
@client.event
async def on_ready():
    change_status.start()
    server_list.start()


#loads cogs:
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


#general ping command:
@client.command(name='ping',
                Description="This command will show you your ping.",
                Brief="Test your ping")
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


#Show list of connected servers in console
@tasks.loop(minutes=15)
async def server_list():
    servers = list(client.guilds)
    clear()
    print("---------------------------------------------------------------------")
    print("Covex bot is online in", str(len(servers)), 'servers:')
    for server in client.guilds:
        print(server.name)
    else:
        print("---------------------------------------------------------------------")
        localtime = time.asctime(time.localtime(time.time()))
        print("Last updated at:",localtime)
        print("---------------------------------------------------------------------")
        print(f'The ping is: {round(client.latency * 1000)}ms')
        print("---------------------------------------------------------------------")


@tasks.loop(seconds=15)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))
client.run('TOKEN')
