from fastapi import FastAPI
from .model import recommender

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Your Movie Recommender API"}

@app.post("/recommendations/")
def get_recommendations(userRatings: dict):
    recommendations = recommender(userRatings)
    return recommendations.head(10).to_dict()