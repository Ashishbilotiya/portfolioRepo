import pickle 
import os

ASE_DIR = os.path.dirname(os.path.abspath(__file__))

famous_books_MODEL_PATH = os.path.join(BASE_DIR, "famous_books.pkl")
books_MODEL_PATH = os.path.join(BASE_DIR, "books.pkl")
books_pt_MODEL_PATH = os.path.join(BASE_DIR, "books_pt.pkl")
books_similarity_score_MODEL_PATH = os.path.join(BASE_DIR, "books_similarity_score.pkl")
movies_MODEL_PATH = os.path.join(BASE_DIR, "movies.pkl")
movies_similarity_score_MODEL_PATH = os.path.join(BASE_DIR, "movies_similarity_score.pkl")

famous_books = pickle.load(open(famous_books_MODEL_PATH,"rb"))
books = pickle.load(open(books_MODEL_PATH,"rb"))
books_pt = pickle.load(open(books_pt_MODEL_PATH,"rb"))
books_similarity_score = pickle.load(open(books_similarity_score_MODEL_PATH,"rb"))
movies = pickle.load(open(movies_MODEL_PATH,"rb"))
movies_similarity_score = pickle.load(open(movies_similarity_score_MODEL_PATH,"rb"))

# print("Models Loaded Successfully")



# famous_books = pickle.load(open(MODEL_PATH,"rb"))
# books = pickle.load(open("books.pkl","rb"))
# books_pt = pickle.load(open("books_pt.pkl","rb"))
# books_similarity_score = pickle.load(open("books_similarity_score.pkl","rb"))
# movies = pickle.load(open("movies.pkl","rb"))
# movies_similarity_score = pickle.load(open("movies_similarity_score.pkl","rb"))
