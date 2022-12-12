import os
from dotenv import load_dotenv
from firebase_admin import credentials
from spotipy.oauth2 import SpotifyOAuth


def SPOTIFY_AUTH():
    load_dotenv()
    scope = "user-read-recently-played"

    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    redirect_uri = os.getenv("REDIRECT_URI")

    auth_manager = SpotifyOAuth(
        client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)

    return auth_manager

def FIRESTORE_CRED():
    load_dotenv()
    cred = credentials.Certificate({
        "type": "service_account",
        "project_id": os.getenv("PROJECT_ID"),
        "private_key": os.getenv("PRIVATE_KEY").replace("\\n", "\n"),
        "client_email": os.getenv("CLIENT_EMAIL"),
        "token_uri": "https://oauth2.googleapis.com/token",
    })
    return cred

if __name__ == "__main__":
    SPOTIFY_AUTH()
