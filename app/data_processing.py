import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix

# Example dataset: user_id, song_id, interaction (play count, rating, etc.)
df = pd.DataFrame({
    "user_id": [1, 2, 3, 1, 2, 3],
    "song_id": [10, 20, 30, 20, 30, 10],
    "interaction": [5, 3, 4, 2, 1, 5]
})

# Mapping IDs
user_map = {user: i for i, user in enumerate(df["user_id"].unique())}
song_map = {song: i for i, song in enumerate(df["song_id"].unique())}

df["user_idx"] = df["user_id"].map(user_map)
df["song_idx"] = df["song_id"].map(song_map)

# Convert to sparse matrix
sparse_matrix = csr_matrix((df["interaction"], (df["user_idx"], df["song_idx"])))