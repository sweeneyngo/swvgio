from api.fetch import createPlaylist, addPlaylistItem, fetchPlaylists
from api.authenticate import validateOAuth2
from collector.search import Collector
from utils.time import getTitle, getDescription, getTime


def main():

    print(getTime())

    youtube = validateOAuth2()

    # check if playlist already exists
    if fetchPlaylists(youtube)["items"][0]["snippet"]["title"] == getTitle():
        print("Playlist already exists! Exiting...")
        exit(0)

    # fetch youtubeIDs
    collector = Collector()
    ids = collector.Fetch()

    # ratelimiting: 10k/day, usage:50-150/mo [POST]
    playlist = createPlaylist(youtube, getTitle(), getDescription())

    # add items based on IDs (need response from playlist)
    for id in ids:
        response = addPlaylistItem(youtube, playlist["id"], id)


if __name__ == "__main__":
    main()
