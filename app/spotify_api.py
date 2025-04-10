import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id="539333315b07401a91f1cd3228b2c06e",
    client_secret="84252701a63b47aab6494661cabf18a9"
))

def get_song_metadata(song_id):
    results = sp.search(q=str(song_id), type="track", limit=1)
    try:
        if results['tracks']['items']:
            track = results['tracks']['items'][0]
            return f"{track['name']} by {track['artists'][0]['name']}"
        return "Unknown Song"
    except Exception as e:
        print("Error fetching song metadata:", e)
        return "Error fetching song metadata"