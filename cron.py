import logging

from utils.spotify import get_data
from db.firestore import add_track_to_db

def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("Running job")
    
    tracks = get_data()

    for track in tracks:
        add_track_to_db(track)

if __name__ == "__main__":
    main()