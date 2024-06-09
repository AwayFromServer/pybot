# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
TARGET_URL = os.getenv('TARGET_URL')
BOT_PREFIX = os.getenv('BOT_PREFIX')

client = discord.Client()

# Bot switches from OFFline to ONline
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    guild_count = 0
    for guild in client.guilds:
        print(f"- {guild.id} (name: {guild.name})")

        guild_count += 1
    
    print("PyBot is running on " + str(guild_count) + " servers.")

# Bot sees a new message
@client.event
async def on_message():
    if message.author == "":
        return
    # slice the array at pos 1, check if BOT_PREFIX was used
    if message.content[:1] == BOT_PREFIX:
        await message.channel.send("Your command was: " + message.content[1:])

# Runs the bot with the predefined event listeners
client.run(BOT_TOKEN)
