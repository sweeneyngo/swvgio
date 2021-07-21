from .gather import parseVG
from utils.verify import grab

"""
@fetch { 
    
    Average rates:
    200-300 GETs/mo. on Collector initialize.

    parseVG() = {usage:bs4, src:https, req:GET, rates:None},
    getVocaIDs() = {usage:requests, src:vocaDB, req:GET (100-150), rates:unknown}
    getYoutubeIDs() = {usage:requests, src:vocaDB, req:GET (100-150), rates:unknown}
    
"""


class Collector:
    def __init__(self):
        self.playlists = parseVG()
        self.vocaIDs = self.__getVocaIDs()
        self.youtubeIDs = self.__getYoutubeIDs()

    def __getVocaIDs(self):
        vocaIDs = []
        nicoIDs = []

        for voca in self.playlists[0]:
            nicoID = voca.link.split("/")[-1]
            nicoIDs.append(nicoID)

        for nicoID in nicoIDs:
            print("Fetching from NND...", end="")
            response = grab(f"https://vocadb.net/api/songs/byPv?pvService=NicoNicoDouga&pvId={nicoID}")
            vocaID = response.json()["id"]
            vocaIDs.append(vocaID)
            print(f"found vocaDB:{vocaID}")

        return vocaIDs

    def __getYoutubeIDs(self):

        youtubeIDs = []

        # must be valid ID for vocaDB database
        if self.vocaIDs is None:
            print("Invalid IDs for vocaDB.")
            return None

        for id in self.vocaIDs:
            print("Fetching from vocaDB...", end="")
            response = grab(f"https://vocadb.net/api/songs/{id}?fields=PVs")
            pvs = response.json()["pvs"]
            for pv in pvs:
                if pv["service"] == "Youtube":
                    youtubeID = pv["url"].split("/")[-1]
                    youtubeIDs.append(youtubeID)
                    print(f"found YT:{youtubeID}")

        return youtubeIDs

    def Fetch(self):
        return self.youtubeIDs
