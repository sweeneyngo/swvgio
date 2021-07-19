from bs4 import BeautifulSoup, SoupStrainer
import httplib2
from utils import time

class Voca: 
    def __init__(self, link, title, artist):
        self.link = link
        self.title = title
        self.artist = artist
    
def parseList():
    http = httplib2.Http()
    status, response = http.request('https://vgperson.com/vocalhighlights.php?m=2021-06')
    # status, response = http.request(time.getSearchQuery())
    
    if status.status != 200:
        print('Couldn\'t fetch resource.')
        return None, None

    playlists = []
    headers = ['Stand-Outs', 'Worth Your Time']

    for index, table in enumerate(BeautifulSoup(response, features="html.parser", parse_only=SoupStrainer('table'))):
        
        playlists.append([])

        videos = table.find_all('td')
        
        # no entries/uneven entries
        if (len(videos) <= 0 or len(videos) % 2 != 0):
            return None, None

        for i in range(0, len(videos), 2):

                
            entry = videos[i].contents
            link = entry[0]['href']
            title = entry[0].contents
            artist = videos[i+1].contents

            if (len(entry) < 1 or len(title) < 1 and not entry[0].has_attr('href') or len(artist) < 1):
                return None, None

            playlists[index].append(Voca(link, title, artist))

    return playlists, headers
