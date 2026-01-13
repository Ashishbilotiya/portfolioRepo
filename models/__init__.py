import pickle 
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
famous_books_PATH = os.path.join(BASE_DIR, "famous_books.pkl")



famous_books = pickle.load(open(famous_books_PATH,"rb"))
books = pickle.load(open("books.pkl","rb"))
books_pt = pickle.load(open("books_pt.pkl","rb"))
books_similarity_score = pickle.load(open("books_similarity_score.pkl","rb"))
movies = pickle.load(open("movies.pkl","rb"))
movies_similarity_score = pickle.load(open("movies_similarity_score.pkl","rb"))
