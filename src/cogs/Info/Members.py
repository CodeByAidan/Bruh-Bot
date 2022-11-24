import discord
from discord.ext import commands
from discord.ext.commands import Bot, BucketType, cooldown
import time 

class members(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_application_command_error(self, ctx, error):
        # sourcery skip: instance-method-first-arg-name
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.respond(error)    
        else:
            raise error    
        
    @commands.slash_command(name="members", description="Get the total amount of members from all servers")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def members(self, ctx):
        total = sum(guild.member_count for guild in self.bot.guilds)
        await ctx.respond(f"Total members: {total}")

def setup(bot):  # sourcery skip: instance-method-first-arg-name
    bot.add_cog(members(bot))