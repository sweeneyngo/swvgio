
def createPlaylist(youtube, title, description):
    request = youtube.playlists().insert(
        part="snippet,status",
        body={
          "snippet": {
            "title": title,
            "description": description,
            "tags": [
              "vocaloid",
              "vgperson"
            ],
            "defaultLanguage": "en"
          },
          "status": {
            "privacyStatus": "public"
          }
        }
    )
    response = request.execute()
    return response