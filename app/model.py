import os
import pandas as pd
import joblib

corr_matrix_path = os.path.join(os.path.dirname(__file__), "corr_matrix.joblib")
corrMatrix = joblib.load(corr_matrix_path)

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