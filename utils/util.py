def transform(data: dict) -> dict:
    """Transform the data into a more usable format.

    Args:
        data (dict): The data to transform.

    Returns:
        dict: The transformed data.
    """
    for item in data['items']:
        item['track'] = _del_available_markets(item['track'])
                
    return data

def _del_available_markets(track: dict) -> dict:
    """Mutate the track object.

    Args:
        track (dict): The track object.

    Returns:
        dict: The mutated track object.
    """
    del track['available_markets']
    del track['album']['available_markets']
    return track