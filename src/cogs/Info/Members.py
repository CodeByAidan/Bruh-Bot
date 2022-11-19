import discord
from discord.ext import commands
from discord.ext.commands import Bot, BucketType, cooldown
import time 

intents = discord.Intents().all()
intents.reactions = True
intents.members = True

bot = Bot(command_prefix="!", intents=intents)
bots = []


class members(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @bot.slash_command(name="members", description="Get the total amount of members from all servers")
    async def members(self, ctx, arg):
        await ctx.send(arg)

    @members.error
    async def members_error(self, ctx, error):
        await ctx.send("There was an error")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("MIssing Required Argument")
        else:
            raise error
    

    # @bot.slash_command(name="members", description="Get the total amount of members from all servers")
    # @commands.cooldown(1, 5, commands.BucketType.user)
    # async def members(self, ctx):
    #     total = sum(guild.member_count for guild in self.bot.guilds)
    #     time.sleep(1)
    #     await ctx.respond(f"Total members: {total}")


def setup(bot):  # sourcery skip: instance-method-first-arg-name
    bot.add_cog(members(bot))
