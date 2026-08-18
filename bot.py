import os

import discord
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)


@bot.event
async def on_ready():
    print(f"Bodyguard est connecté en tant que {bot.user}")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == "!ping":
        await message.channel.send("🛡️ Pong !")


bot.run(token)