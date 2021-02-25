from discord import Embed
from datetime import datetime
import random


async def fast_random(ctx):
    random_number = random.randint(0, 100)
    embed = Embed(title=random_number,
                  colour=ctx.author.colour,
                  timestamp=datetime.utcnow())
    await ctx.send(embed=embed)


async def get_random_number(ctx, floor, ceil):
    embed = Embed(title="GENERÁTOR NÁHODNÝCH ČÍSEL",
                  colour=ctx.author.colour,
                  timestamp=datetime.utcnow())
    random_number = random.randint(int(floor), int(ceil))

    if not floor:
        await ctx.send("Zadejte příkaz ve formátu .rng {menší číslo} {větší číslo}")
    fields = [("Náhodné číslo mezi {} a {}".format(floor, ceil), random_number, True)]

    for name, value, inline in fields:
        embed.add_field(name=name, value=value, inline=inline)
    await ctx.send(embed=embed)
