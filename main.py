from api.fetch import createPlaylist, addPlaylistItem, fetchPlaylists
from api.authenticate import validateOAuth2
from collector.search import Collector
from utils.time import getTitle, getDescription, getTime
import schedule
import time


def job():
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
    print("Creating playlist . . .")
    playlist = createPlaylist(youtube, getTitle(), getDescription())

    # add items based on IDs (need response from playlist)
    print("Adding playlist items . . .")
    for id in ids:
        response = addPlaylistItem(youtube, playlist["id"], id)

    print("Successfully created playlist!")


def main():
    schedule.every(2).weeks.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
