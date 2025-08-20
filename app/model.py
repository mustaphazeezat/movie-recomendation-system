import os
import pandas as pd
import joblib


#   Load the sparse correlation matrix

corr_matrix_path = os.path.join(os.path.dirname(__file__), "corr_matrix_sparse.joblib")
sparse_matrix, movie_titles = joblib.load(corr_matrix_path)
corrMatrix = pd.DataFrame(sparse_matrix.toarray(), index=movie_titles, columns=movie_titles)



def recommender(userRatingDict):
    similarMovies = pd.Series(dtype='float64')
    
    for movieTitle, rating in userRatingDict.items():
        similar = corrMatrix[movieTitle].dropna()
        similar = similar.map(lambda x: x * rating )
        
        similarMovies = similarMovies.add(similar, fill_value=0)
        
    # Remove the movies the user already rated
    similarMovies = similarMovies.drop(labels=userRatingDict.keys(), errors="ignore")    
    similarMovies = similarMovies.sort_values(ascending=False)
        
    return similarMovies