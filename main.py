#!/env/bin/python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from api import createPlaylist, getChannel, search, addPlaylistItem
from collector import gather
from utils import time

scopes = ["https://www.googleapis.com/auth/youtube.readonly", "https://www.googleapis.com/auth/youtube.force-ssl"]
vgid = "UCkkAwQwkwmDHTPuxr2Q7Z1g"

def main():
      # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    client_secret = "client_secret_899475630692-9ged7luqiefjle1l6dbtq70sinigk0ui.apps.googleusercontent.com.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secret, scopes)

    youtube = googleapiclient.discovery.build(
        'youtube', 'v3', credentials=flow.run_console())

    # list vgperson's recommendations
    playlists, headers = gather.parseList()
    if (playlists and headers):
        print(headers)

    # funnel into playlist IDs
    ids = []
    for voca in playlists[0]:
        query = ' '.join(voca.title + voca.artist)
        response = search.search(youtube, query)

        if (response['pageInfo']['resultsPerPage'] >= 1 and response['items'] != []):
            for i in range(len(response['items'])):
                if response['items'][i]['id']['kind'] == "youtube#video":
                    ids.append(response['items'][i]['id']['videoId'])
                    break

        else:
            print('None')

    print(ids)

    response = createPlaylist.createPlaylist(youtube, time.getTitle(), time.getDescription())
    
    # add items based on IDs (need response from playlist)
    for id in ids:
        response = addPlaylistItem.addPlaylistItem(youtube, '''playlist_id''', id)

    # response = getChannel.getChannel(youtube, vgid)
    # print(response)

if __name__ == "__main__":
    main()