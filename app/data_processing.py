import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix

def prepare_sparse_matrix(file_path):
    """
    Reads interaction data from a CSV file and converts it into a sparse matrix.
    :param file_path: Path to the CSV file containing interaction data.
    :return: A sparse matrix of interactions.
    """
    # Read the interaction data
    df = pd.read_csv(file_path)

    # Ensure the required columns exist
    if not {'user_id', 'song_id', 'interaction'}.issubset(df.columns):
        raise ValueError("CSV file must contain 'user_id', 'song_id', and 'interaction' columns.")

    # Map user and song IDs to indices
    user_map = {user: i for i, user in enumerate(df["user_id"].unique())}
    song_map = {song: i for i, song in enumerate(df["song_id"].unique())}

    df["user_idx"] = df["user_id"].map(user_map)
    df["song_idx"] = df["song_id"].map(song_map)

    # Convert to a sparse matrix
    sparse_matrix = csr_matrix((df["interaction"], (df["user_idx"], df["song_idx"])))

    return sparse_matrix