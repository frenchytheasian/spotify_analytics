import spotipy

from utils.credentials import SPOTIFY_AUTH

sp = spotipy.Spotify(auth_manager=SPOTIFY_AUTH())

def get_data():
    results = sp.current_user_recently_played(limit=50)
    tracks = results['items']
    return tracks

def search_track(raw_track: dict):
    query = f"artist:{raw_track['artistName']} track:{raw_track['trackName']}"
    result = sp.search(query, limit=1)
    return result