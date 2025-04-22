import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="539333315b07401a91f1cd3228b2c06e",
    client_secret="84252701a63b47aab6494661cabf18a9",redirect_uri="http://localhost:8888/callback",
    scope="user-top-read"
))

def get_user_top_tracks_and_artists():
    """
    Fetches the user's top tracks and artists from Spotify.
    """
    # Get user's top tracks
    top_tracks = sp.current_user_top_tracks(limit=10, time_range='short_term')
    track_ids = [track['id'] for track in top_tracks['items']]
    
    # Get user's top artists
    top_artists = sp.current_user_top_artists(limit=10, time_range='short_term')
    artist_ids = [artist['id'] for artist in top_artists['items']]
    
    return track_ids, artist_ids

def get_spotify_recommendations(seed_tracks, seed_artists, n_recommendations=20):
    """
    Fetches song recommendations from Spotify's API based on seed tracks and artists.
    """
    recommendations = sp.recommendations(seed_tracks=seed_tracks[:5], seed_artists=seed_artists[:5], limit=n_recommendations)
    recommended_track_ids = [track['id'] for track in recommendations['tracks']]
    return recommended_track_ids

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