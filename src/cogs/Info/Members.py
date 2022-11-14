import discord
from discord.ext import commands
from discord.ext.commands import Bot

intents = discord.Intents().all()
intents.reactions = True
intents.members = True

bot = Bot(command_prefix=".", intents=intents)
bots = []

class members(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.slash_command(name="members", description="Get the total amount of members from all servers")
    async def members(self, ctx):
        total = sum(guild.member_count for guild in self.bot.guilds)
        await ctx.respond(f"Total members: {total}")


def setup(bot):
  bot.add_cog(members(bot))