import logging
import time
import sys

from utils.spotify import get_data
from db.firestore import add_track_to_db


def main():
    sleep_amount = sys.argv[1]
    try:
        int(sleep_amount)
    except ValueError:
        sys.exit(
            "Please enter a valid integer for the amount of minutes to wait between queries.")

    while True:
        logging.basicConfig(level=logging.INFO)
        logging.info("Running job")

        tracks = get_data()

        for track in tracks:
            add_track_to_db(track)

        time.sleep(int(sleep_amount) * 60)


if __name__ == "__main__":
    main()
