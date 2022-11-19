import datetime
import os

import discord
import dotenv
import requests
from discord.ext import commands
from discord.ext.commands import Bot

dotenv.load_dotenv()

intents = discord.Intents().all()
intents.reactions = True
intents.members = True

bot = Bot(command_prefix=".", intents=intents)
bots = []


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.slash_command(
        name="weather", description="Get the weather for a given location"
    )
    async def weather(self, ctx, *, city: str):
        # sourcery skip: instance-method-first-arg-name, use-fstring-for-concatenation
        api_key = os.getenv("OPENWEATHERMAP_KEY")
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = city
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_temperature_celsiuis = str(round(current_temperature - 273.15))
            current_temperature_fahrenheit = str(
                round((current_temperature - 273.15) * 9 / 5 + 32)
            )
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            weather_description = z[0]["description"]
            if z[0]["icon"] == "01d":
                color = 0x87CEEB
            elif z[0]["icon"] == "01n":
                color = 0x87CEEB
            elif z[0]["icon"] == "02d":
                color = 0x5779C7
            elif z[0]["icon"] == "02n":
                color = 0x5779C7
            elif z[0]["icon"] == "03d":
                color = 0xACBDE3
            elif z[0]["icon"] == "03n":
                color = 0xACBDE3
            elif z[0]["icon"] == "04d":
                color = 0x8495BD
            elif z[0]["icon"] == "04n":
                color = 0x8495BD
            elif z[0]["icon"] == "09d":
                color = 0xCCCACA
            elif z[0]["icon"] == "09n":
                color = 0xCCCACA
            elif z[0]["icon"] == "10d":
                color = 0xCCCACA
            elif z[0]["icon"] == "10n":
                color = 0xCCCACA
            elif z[0]["icon"] == "11d":
                color = 0x828080
            elif z[0]["icon"] == "11n":
                color = 0x828080
            elif z[0]["icon"] == "13d":
                color = 0xFFFAFA
            elif z[0]["icon"] == "13n":
                color = 0xFFFAFA
            elif z[0]["icon"] == "50d":
                color = 0xD7D7D7
            elif z[0]["icon"] == "50n":
                color = 0xD7D7D7
            else:
                color = 0xFF0000                           
            embed = discord.Embed(
                title=f"Weather in {city_name}",
                color= color,
                timestamp=datetime.datetime.now(datetime.timezone.utc),
            )

            embed.add_field(
                name="Descripition", value=f"**{weather_description}**", inline=False
            )
            embed.add_field(
                name="Temperature(F)",
                value=f"**{current_temperature_fahrenheit}°F**",
                inline=True,
            )
            embed.add_field(
                name="Temperature(C)",
                value=f"**{current_temperature_celsiuis}°C**",
                inline=True,
            )
            embed.add_field(
                name="Humidity(%)", value=f"**{current_humidity}%**", inline=False
            )
            embed.add_field(
                name="Atmospheric Pressure(hPa)",
                value=f"**{current_pressure}hPa**",
                inline=False,
            )
            embed.add_field(
                name="Wind Speed(m/s)",
                value=f"**{x['wind']['speed']}m/s**",
                inline=False,
            )
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            embed.set_thumbnail(
                url=f"http://openweathermap.org/img/w/{str(x['weather'][0]['icon'])}.png"
            )
            await ctx.respond(embed=embed)
        else:
            await ctx.respond("City not found.")


def setup(bot):
    bot.add_cog(Commands(bot))
