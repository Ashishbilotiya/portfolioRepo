import pickle 
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

famous_books_MODEL_PATH = os.path.join(BASE_DIR, "famous_books.pkl")
books_MODEL_PATH = os.path.join(BASE_DIR, "books.pkl")
books_pt_MODEL_PATH = os.path.join(BASE_DIR, "books_pt.pkl")
books_similarity_score_MODEL_PATH = os.path.join(BASE_DIR, "books_similarity_score.pkl")
movies_MODEL_PATH = os.path.join(BASE_DIR, "movies.pkl")
movies_similarity_score_MODEL_PATH = os.path.join(BASE_DIR, "movies_similarity_score.pkl")


def load_famous_books():
    famous_books = None
    if famous_books is None:
        with open(famous_books_MODEL_PATH, "rb") as f:
            famous_books = pickle.load(f)
    return famous_books

def load_books():
    books = None
    if books is None:
        with open(books_MODEL_PATH, "rb") as f:
            books = pickle.load(f)
    return books

def load_books_pt():
    books_pt = None
    if books_pt is None:
        with open(books_pt_MODEL_PATH, "rb") as f:
            books_pt = pickle.load(f)
    return books_pt

def load_books_similarity_score():
    books_similarity_score = None
    if books_similarity_score is None:
        with open(books_similarity_score_MODEL_PATH, "rb") as f:
            books_similarity_score = pickle.load(f)
    return books_similarity_score

def load_movies():
    movies = None
    if movies is None:
        with open(movies_MODEL_PATH, "rb") as f:
            movies = pickle.load(f)
    return movies

def load_movies_similarity_score():
    movies_similarity_score = None
    if movies_similarity_score is None:
        with open(movies_similarity_score_MODEL_PATH, "rb") as f:
            movies_similarity_score = pickle.load(f)
    return movies_similarity_score




