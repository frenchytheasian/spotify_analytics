import json
import time

import spotipy
import firebase_admin
from firebase_admin import firestore

from credentials import SPOTIFY_AUTH, FIRESTORE_CRED

sp = spotipy.Spotify(auth_manager=SPOTIFY_AUTH())

firebase_admin.initialize_app(FIRESTORE_CRED())
db = firestore.client()

def add_track_to_db(track: dict):
    """Add a track to the database.

    Args:
        track (dict): The track to add.
    """
    db_id = track['played_at']
    track_ref = db.collection(u'tracks').document(db_id)
    track_ref.set(track)

def main():
    results = sp.current_user_recently_played(limit=50)
    tracks = results['items']
    
    for track in tracks:
        add_track_to_db(track)
        
    
if __name__ == "__main__":
    main()
