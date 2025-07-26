from utils.spotify_utils import search_tracks

def format_track_data(track):
    return {
        'name': track['name'],
        'artist': track['artists'][0]['name'],
        'url': track['external_urls']['spotify']
    }

def get_recommendations(mood):
    tracks = search_tracks(mood, limit=4)['tracks']
    print(tracks)
    result = []
    for item in tracks['items']:
        result.append(format_track_data(item))
    return result
