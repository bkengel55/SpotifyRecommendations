import implicit
from app.data_processing import prepare_sparse_matrix
from app.spotify_api import get_song_metadata
from implicit.als import AlternatingLeastSquares

sparse_matrix = prepare_sparse_matrix("data/interactions.csv")

# Convert interaction matrix to a format suitable for implicit
sparse_matrix = sparse_matrix.T  # Implicit assumes (items, users) matrix

# Train ALS Model
als_model = implicit.als.AlternatingLeastSquares(factors=50, regularization=0.1, iterations=20)
als_model.fit(sparse_matrix.T)  # Fit the model on the transposed matrix

def get_recommendations(user_id, n_recommendations):
    """
    Generates song recommendations for a user.
    """
    # Use ALS model to recommend items for the user
    recommendations = als_model.recommend(user_id, sparse_matrix[user_id], N=n_recommendations)

    # Convert recommendations to a user-friendly format (e.g., fetch song names)
    song_names = [get_song_metadata(song_id) for song_id, _ in recommendations]
    
    return song_names

