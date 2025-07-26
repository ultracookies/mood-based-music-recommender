# Placeholder for logic based on mood (can map to Spotify valence/energy)
def get_recommendations(mood):
    # This would normally hit Spotify's API or your own dataset
    mood_map = {
        "Happy": ["track_1", "track_2"],
        "Sad": ["track_3", "track_4"]
    }
    # You'd replace this with API calls + filtering
    return [{
        "name": "Mock Song",
        "artist": "Mock Artist",
        "url": "https://open.spotify.com/track/mockid"
    }]


def get_suggestions(mood):
    pass
