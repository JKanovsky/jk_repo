import discord
import random

async def random_image(ctx):
    f = open("newtextfile.txt", "r")
    split_string = str(f.read()).split(":")
    img = random.randint(0, len(split_string))

    await ctx.send(file=discord.File(split_string[img]))