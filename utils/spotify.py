import spotipy

from utils.credentials import SPOTIFY_AUTH

sp = spotipy.Spotify(auth_manager=SPOTIFY_AUTH())

def get_data():
    results = sp.current_user_recently_played(limit=50)
    tracks = results['items']
    return tracks