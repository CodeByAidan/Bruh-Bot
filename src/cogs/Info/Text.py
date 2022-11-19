import discord
from discord.ext import commands
from discord.ext.commands import Bot, cooldown, BucketType
import dotenv
import os
from twilio.rest import Client 
import datetime

dotenv.load_dotenv()

intents = discord.Intents().all()
intents.reactions = True
intents.members = True

bot = Bot(command_prefix=".", intents=intents)

class text(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
            
    @bot.slash_command(
        name="text", description="Send a SMS text message to the owner of the bot"
    )
    async def text(self, ctx, *, message: str):
        try:
            if len(message) > 160:
                await ctx.respond("Message must be less than 160 characters")
            elif all(ord(c) < 128 for c in message):                                
                # sourcery skip: instance-method-first-arg-name
                account_sid = os.getenv('TWILIO_ACCOUNT_SID')
                auth_token = os.getenv('TWILIO_AUTH_TOKEN')
                client = Client(account_sid, auth_token)
                msg = client.messages.create(
                    body=f"Discord: '{ctx.author.name}' said:\n{message}",
                    from_=os.getenv('TWILIO_PHONE_NUMBER'),
                    to=os.getenv('PHONE_NUMBER')
                )
                print(f"Message SID: {msg.sid}")
                print(f"Text message sent to: {os.getenv('PHONE_NUMBER')}!")

                embed=discord.Embed(
                    title="Sent!",
                    description=f"Message was received successfully!\nMessage contents: {message}",
                    timestamp=datetime.datetime.now(datetime.timezone.utc),
                    color=0x00ff2a
                )
                embed.set_author(
                    name=f"{ctx.author.name}",
                    icon_url=f"{ctx.author.avatar.url}"
                )
                embed.set_thumbnail(
                    url="https://i.imgflip.com/6g1ntj.jpg"
                )
                embed.set_footer(
                    text=f"Requested by {ctx.author.name}"
                )
                await ctx.respond(embed=embed)

        except Exception as e:
            os.system("cls")
            print(e)
            embed=discord.Embed(
                title="Error!",
                description=f"Message was not received successfully!\nMessage contents: {message}",
                color=0xff0000
            )
            embed.set_author(
                name=f"{ctx.author.name}",
                icon_url=f"{ctx.author.avatar.url}"
            )
            embed.set_thumbnail(
                url="https://i.imgflip.com/6g1ntj.jpg"
            )
            embed.set_footer(
                text=f"Sent at: {datetime.datetime.now(datetime.timezone.utc)}"
            )
            await ctx.respond(embed=embed)
            

def setup(bot):
    bot.add_cog(text(bot))
