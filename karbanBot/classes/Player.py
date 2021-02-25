class Player:
    def __init__(self, summonerId, summonerName, champion, team, gameMode):
        self.summonerId = summonerId
        self.summonerName = summonerName
        self.champion = champion
        self.team = team
        self.gameMode = gameMode

    def get_gameMode_name(self):
        if self.gameMode == 400:
            return "Draft Pick"
        if self.gameMode == 420:
            return "Ranked Solo/Duo"
        if self.gameMode == 430:
            return "Blind Pick"
        if self.gameMode == 440:
            return "Ranked Flex"
        if self.gameMode == 450:
            return "ARAM"
        if not isinstance(self.gameMode, str):
            return "Jiný herní mód"

    def get_champion(self):
        f = open("champData.txt", "r")
        splitted = str(f.read()).split(":")
        for i in range(0, len(splitted), 2):
            if str(self.champion) == str(splitted[i]):
                return splitted[i + 1]