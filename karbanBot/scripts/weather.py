import api
import requests
from discord import Embed
from datetime import datetime
import unidecode


async def get_weather_info(ctx, city):
    embed = Embed(title="Karbanové počasí",
                  colour=ctx.author.colour,
                  timestamp=datetime.utcnow())
    try:
        uni_city = unidecode.unidecode(city)
        response = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={uni_city}&units=metric&lang=cz&appid={api.WEATHER_API_KEY}")
        content = response.json()

        fields = getFields(content)
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
        await ctx.send(embed=embed)

    except Exception:
        try:
            response = requests.get(
                f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=cz&appid={api.WEATHER_API_KEY}")
            content = response.json()

            fields = getFields(content)
            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
            await ctx.send(embed=embed)

        except Exception:
            await ctx.send("Špatně zadané město")


def getFields(content):
    return [
        ("Město: ", content['name'], True),
        ("Země: ", content['sys']['country'], True),
        ("Teplota: ", content['main']['temp'], False),
        ("Pocitová teplota: ", content['main']['feels_like'], True),
        ("Srážky", content['main']['humidity'],False),
        ("stav na nebi: ", content['weather'][0]['description'], False)
    ]