from this import d
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                        client_secret=client_secret))

def search(search, limit):
    results = sp.search(q=search, limit=limit)
    for idx, track in enumerate(results['tracks']['items']):
        print(idx, track['name'])