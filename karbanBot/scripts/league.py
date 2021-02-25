import requests
import api
from classes.Player import Player
from discord import Embed
from datetime import datetime


def get_id(target):
    response = requests.get("{}/summoner/v4/summoners/by-name/{}?api_key={}"
                            .format(api.EUN1_HTTP_LINK, target, api.RIOT_API_TOKEN))

    content = response.json()
    id = content['id']
    print(id)
    return id


async def league_info(ctx, target):
    playerId = get_id(target)
    player_list = get_live_game(playerId)
    readable_gameMode = player_list[0].get_gameMode_name()

    for v in player_list:
        v.champion = v.get_champion()

    embed = Embed(title="Herní mód: {}".format(readable_gameMode),
                  colour=ctx.author.colour,
                  timestamp=datetime.utcnow())

    fields = [("Modrý tým", [
                "{} hraje {} ".format(player_list[v].summonerName, player_list[v].champion) if player_list[v].team == 100 else 0 for v in range(0, 5)], False),
              ("Červený tým", [
                  "{} hraje {} ".format(player_list[v].summonerName, player_list[v].champion) if player_list[v].team == 200 else 0
                  for v in range(5, 10)], False)
              ]

    for name, value, inline in fields:
        embed.add_field(name=f'**{name}**', value=f'{value[0]}\n{value[1]}\n{value[2]}\n{value[3]}\n{value[4]}',
                        inline=inline)
    await ctx.send(embed=embed)


def get_live_game(player_id):
    response = requests.get("{}/spectator/v4/active-games/by-summoner/{}?api_key={}"
                            .format(api.EUN1_HTTP_LINK, player_id, api.RIOT_API_TOKEN))
    if response == 404:
        return 404
    if response == 403:
        return 403
    content = response.json()
    player_data = content['participants']
    player_list = []
    for summoner in player_data:
        id = summoner['summonerId']
        name = summoner['summonerName']
        champion = summoner['championId']
        team = summoner['teamId']
        gameMode = content['gameQueueConfigId']
        player_list.append(Player(id, name, champion, team, gameMode))
    return player_list