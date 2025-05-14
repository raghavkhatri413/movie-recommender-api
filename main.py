# main.py

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from knn_model import recommend_movies, search_movies

app = FastAPI()

# CORS for React Native
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict to mobile app domain later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Movie Recommender API is running."}

@app.get("/search")
def search(query: str = Query(..., min_length=1)):
    return {"results": search_movies(query)}

@app.get("/recommend")
def recommend(movie: str, top_n: int = 10):
    return {"results": recommend_movies(movie, top_n=top_n)}
# main.py

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from knn_model import recommend_movies, search_movies

app = FastAPI()

# CORS for React Native
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict to mobile app domain later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Movie Recommender API is running."}

@app.get("/search")
def search(query: str = Query(..., min_length=1)):
    return {"results": search_movies(query)}

@app.get("/recommend")
def recommend(movie: str, top_n: int = 10):
    return {"results": recommend_movies(movie, top_n=top_n)}
