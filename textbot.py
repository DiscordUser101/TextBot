import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import Bot

Client = discord.Client()
bot_prefix = "---"
client = commands.Bot(command_prefix = bot_prefix)

@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))


@client.event
async def on_message(message):
    if message.content.upper().startswith('!SAY'):
        args = message.content.split(" ")
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))

client.login(process.env.BOT_TOKEN)
