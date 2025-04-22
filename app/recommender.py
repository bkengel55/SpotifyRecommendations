import implicit
from app.data_processing import prepare_sparse_matrix
from app.spotify_api import get_song_metadata, get_spotify_recommendations, get_user_top_tracks_and_artists
from implicit.als import AlternatingLeastSquares

sparse_matrix = prepare_sparse_matrix("data/interactions.csv")

# Convert interaction matrix to a format suitable for implicit
sparse_matrix = sparse_matrix.T  # Implicit assumes (items, users) matrix

# Train ALS Model
als_model = implicit.als.AlternatingLeastSquares(factors=50, regularization=0.1, iterations=20)
als_model.fit(sparse_matrix.T)  # Fit the model on the transposed matrix

def get_recommendations_with_user_data(user_id, n_recommendations):
    """
    Generates song recommendations for a user.
    """
    # Fetch user's top tracks and artists
    track_ids, artist_ids = get_user_top_tracks_and_artists()
    spotify_recommendations = get_spotify_recommendations(track_ids, artist_ids, n_recommendations)
    # Use ALS model to recommend items for the user
    recommendations = als_model.recommend(user_id, sparse_matrix[user_id], N=n_recommendations)

    # Combine and deduplicate recommendations
    combined_recommendations = list(set([song_id for song_id, _ in recommendations] + spotify_recommendations))

    # Filter or prioritize recommendations based on user's top tracks/artists
    filtered_recommendations = [
        (song_id, score) for song_id, score in combined_recommendations
        if song_id in track_ids or song_id in artist_ids
    ]

    # If no recommendations match, use the top ALS recommendations
    if not filtered_recommendations:
        filtered_recommendations = combined_recommendations

    # Sort by score (descending)
    filtered_recommendations.sort(key=lambda x: x[1], reverse=True)

    # Limit to n_recommendations
    recommendations = filtered_recommendations[:n_recommendations]

    # Convert recommendations to a user-friendly format (e.g., fetch song names)
    song_names = [get_song_metadata(song_id) for song_id, _ in recommendations]
    
    return song_names

