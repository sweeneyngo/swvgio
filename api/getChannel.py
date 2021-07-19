
def getChannel(youtube, id):
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id=id
    )
    response = request.execute()
    return response