import os
import discord
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)


def get_security_channel(guild):
    return discord.utils.get(
        guild.text_channels,
        name="🔐-security-logs"
    )


@bot.event
async def on_ready():
    print(f"Bodyguard est connecté en tant que {bot.user}")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == "!ping":
        await message.channel.send("🛡️ Pong !")

    if "phishing" in message.content.lower():
        channel = get_security_channel(message.guild)

        if channel:
            await channel.send(
                f"⚠️ Mot-clé suspect détecté : "
                f"`phishing` dans le message de {message.author.mention}."
            )


@bot.event
async def on_member_join(member):
    channel = get_security_channel(member.guild)

    if channel:
        await channel.send(
            f"🚨 Nouveau membre : {member.mention} "
            f"a rejoint le serveur."
        )


bot.run(token)
