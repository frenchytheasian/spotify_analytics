from datetime import datetime, timezone

import firebase_admin
from firebase_admin import firestore

from utils.credentials import FIRESTORE_CRED

firebase_admin.initialize_app(FIRESTORE_CRED())
db = firestore.client()

def add_track_to_db(track: dict):
    """Add a track to the database.

    Args:
        track (dict): The track to add.
    """
    # dt stands for datetime
    try:
        dt = datetime.strptime(track['played_at'], "%Y-%m-%dT%H:%M:%S.%fZ")
    except ValueError:
        dt = datetime.strptime(track['played_at'], "%Y-%m-%dT%H:%M:%SZ")
    dt = dt.replace(tzinfo=timezone.utc).astimezone(tz=None)
    
    track_ref = db.collection(str(dt.date())).document(str(dt))
    track_ref.set(track)