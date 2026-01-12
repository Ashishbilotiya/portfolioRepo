import pickle 


famous_books = pickle.load(open("src/models/famous_books.pkl","rb"))
books = pickle.load(open("src/models/books.pkl","rb"))
books_pt = pickle.load(open("src/models/books_pt.pkl","rb"))
books_similarity_score = pickle.load(open("src/models/books_similarity_score.pkl","rb"))
movies = pickle.load(open("src/models/movies.pkl","rb"))
movies_similarity_score = pickle.load(open("src/models/movies_similarity_score.pkl","rb"))