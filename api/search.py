
def search(youtube, query):
    request = youtube.search().list(
        part="snippet",
        maxResults=5,
        q=query
    )
    response = request.execute()
    return response