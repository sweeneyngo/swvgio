from googleapiclient.errors import HttpError
import time


def createPlaylist(youtube, title, description):
    request = youtube.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "tags": ["vocaloid", "vgperson"],
                "defaultLanguage": "en",
            },
            "status": {"privacyStatus": "public"},
        },
    )
    response = request.execute()
    return response


def getChannel(youtube, id):
    request = youtube.channels().list(part="snippet,contentDetails,statistics", id=id)
    response = request.execute()
    return response


def search(youtube, query):
    request = youtube.search().list(part="snippet", maxResults=5, q=query)
    response = request.execute()
    return response


def checkBannedCountries(youtube, id):
    request = youtube.videos().list(part="snippet,contentDetails", id=id)
    response = request.execute()

    try:
        query = response["items"][0]["contentDetails"]["regionRestriction"]["blocked"]
    except (IndexError, KeyError) as err:
        return

    return query


def checkDescription(youtube, id):
    request = youtube.videos().list(part="snippet,contentDetails", id=id)
    response = request.execute()

    try:
        query = response["items"][0]["snippet"]["description"]
    except (KeyError, IndexError) as err:
        print(err)
        print("Failed to fetch the video's description. Skipping...")
        return

    return query


def addPlaylistItem(youtube, playlist_id, video_id):
    request = youtube.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": playlist_id,
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": video_id,
                },
            }
        },
    )

    response = request.execute()
    return response


def checkPlaylistCount(youtube, id):
    request = youtube.playlistItems().list(part="snippet", playlistId=id)

    try:
        response = request.execute()
        query = response["pageInfo"]["totalResults"]
    except HttpError as err:
        # If the error is a rate limit or connection error,
        # wait and try again.
        print("? ", err.code)

        if err.resp.status in [404]:
            print("Playlist doesn't exist.")
            print(f"An HTTP error {err.code} occurred:{err.reason}")
            print("Sleeping for 5 seconds...")
            time.sleep(5)

        elif err.resp.status in [403, 500, 503]:
            print(f"An HTTP error {err.code} occurred:{err.reason}")
            print("Sleeping for 5 seconds...")
            time.sleep(5)
        else:
            raise

    except (KeyError, IndexError) as err:
        print(err)
        print("Failed to fetch the playlist's video count. Skipping...")
        return

    return query


def listVideos(youtube):
    request = youtube.videos().list(part="snippet,contentDetails,statistics", id="lw7pcm1W5tw")
    response = request.execute()
    return response


def fetchPlaylists(youtube):
    request = youtube.playlists().list(part="snippet,contentDetails", maxResults=5, mine=True)
    response = request.execute()
    return response
