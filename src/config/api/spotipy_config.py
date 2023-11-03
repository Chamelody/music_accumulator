import os

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(
    client_id=os.getenv('SPOTIFY_API_CLIENT_ID'),
    client_secret=os.getenv('SPOTIFY_API_CLIENT_SECRET')
)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
