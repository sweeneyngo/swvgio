from bs4 import BeautifulSoup, SoupStrainer
import httplib2


class Voca:
    def __init__(self, link, title, artist):
        self.link = link
        self.title = title
        self.artist = artist


"""

@return [
            [Voca(link, title, artist), ... ], 
            [Voca(link, title, artist), ... ],
        ]
@extra {len(return) = 2}

"""


def parseVG():

    # http client
    http = httplib2.Http()

    try:
        status, response = http.request("https://vgperson.com/vocalhighlights.php?m=2021-06")
        # status, response = http.request(getSearchQuery())
    except httplib2.ServerNotFoundError:
        print("Couldn't fetch resource.")
        return None, None

    playlists = []

    for index, table in enumerate(BeautifulSoup(response, features="html.parser", parse_only=SoupStrainer("table"))):

        playlists.append([])

        videos = table.find_all("td")

        # no entries/uneven entries
        if len(videos) <= 0 or len(videos) % 2 != 0:
            return None, None

        for i in range(0, len(videos), 2):

            entry = videos[i].contents or []
            link = entry[0]["href"] or []
            title = entry[0].contents or []
            artist = videos[i + 1].contents or []

            if not (entry and title and artist and link):
                return None, None

            playlists[index].append(Voca(link, title, artist))

    return playlists
