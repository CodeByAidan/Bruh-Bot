import logging
import os
import os.path

import discord
import dotenv
import requests
from discord.ext import tasks
from discord.ext.commands import Bot

intents = discord.Intents().all()
intents.reactions = True
intents.members = True

logging.basicConfig(level=logging.INFO)

dotenv.load_dotenv()

bot = Bot(command_prefix="-", intents=intents)
token = os.getenv("TOKEN")
bot.remove_command("help")


for filename in os.listdir(r"cogs/Info"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.Info.{filename[:-3]}")
        print(f"{filename} loaded!")

# Get total amount of members from all servers


@bot.event
async def on_ready():
    os.system("cls")
    print("Bot in server: Success")
    print(f"Bot name: {bot.user.name}")
    statement = "servers" if len(bot.guilds) > 1 else "server"
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=f"{len(bot.guilds)} {statement} and {len(bot.users)} users",
        )
    )


# run token
bot.run(token)
