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
    except KeyError or IndexError:
        return

    return query


def checkDescription(youtube, id):
    request = youtube.videos().list(part="snippet,contentDetails", id=id)
    response = request.execute()

    try:
        query = response["items"][0]["snippet"]["description"]
    except KeyError or IndexError:
        print("Failed to fetch the video's description. Skipping...")
        return

    return query


def addPlaylistItem(youtube, playlist_id, video_id):
    print(video_id)

    request = youtube.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": playlist_id,
                "position": 0,
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
    response = request.execute()

    try:
        query = response["pageInfo"]["totalResults"]
    except KeyError or IndexError:
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
