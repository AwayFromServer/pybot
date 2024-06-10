"""_summary_
"""
import os

import urllib.request

import discord
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
TARGET_URL = os.getenv('TARGET_URL')
BOT_PREFIX = os.getenv('BOT_PREFIX')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
#client = discord.Client()

async def status(m):
    """
    status(m) takes in message from on_message(m) event,
    checks TARGET_URL based on status code
    """
    if urllib.request.urlopen(TARGET_URL).getcode() == 200:
        await m.channel.send("It looks like it's up! " + TARGET_URL)
    else:
        await m.channel.send("It looks like it's offline... " + TARGET_URL)

@client.event
async def on_ready():
    """Event handler indicating we're ONLINE!"""
    print(f'{client.user} has connected to Discord!')

    guild_count = 0
    for guild in client.guilds:
        print(f"- {guild.id} (name: {guild.name})")

        guild_count += 1
    print("PyBot is running on " + str(guild_count) + " servers.")

@client.event
async def on_message(m):
    """Event handler for message received that is visible to the bot"""
    print(m.content)
    if m.author == client.user:
        return
    # slice the array at pos 1, check if BOT_PREFIX was used
    elif m.content[:1] == BOT_PREFIX:
        match m.content[1:]:
            # list of possible commands
            case "status":
                await status(m)
                return
            case _:
                return
    # general responses
    elif m.content.find("server status") != -1:
        await m.channel.send("Try using !status")
    elif m.content.find("bot") != -1:
        await m.channel.send("Who, me?")

# Runs the bot with the predefined event listeners
client.run(BOT_TOKEN)
