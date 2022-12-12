import spotipy

from utils.credentials import SPOTIFY_AUTH
from db.firestore import add_track_to_db

sp = spotipy.Spotify(auth_manager=SPOTIFY_AUTH())


def main():
    results = sp.current_user_recently_played(limit=50)
    tracks = results['items']

    for track in tracks:
        add_track_to_db(track)

if __name__ == "__main__":
    main()