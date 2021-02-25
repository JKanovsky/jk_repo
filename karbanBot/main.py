import api
import scripts.number_generator
import scripts.league
import scripts.image
import scripts.weather


@api.client.event
async def on_ready():
    print("bot is ready")


@api.client.command(name="fast-rnd", aliases=["rnd"])
async def get_number_in_static_range(ctx):
    await scripts.number_generator.fast_random(ctx)


@api.client.command(name="rng_in_range", aliases=["rng"])
async def get_number_in_flexible_range(ctx):
    await scripts.number_generator.get_random_number(ctx)


@api.client.command(name="lolinfo", aliases=["lol"])
async def get_league_game_data(ctx, target):
    await scripts.league.league_info(ctx, target)


@api.client.command(name="image")
async def get_image_from_file(ctx):
    await scripts.image.random_image(ctx)


@api.client.command(name="pocasi", aliases=["weather"])
async def get_weather_info(ctx, city):
    await scripts.weather.get_weather_info(ctx, city)


api.client.run(api.DISCORD_TOKEN)
