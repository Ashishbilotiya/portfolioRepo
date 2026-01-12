import numpy as np
from models import *



def BookRecommend(book_name):
    book_index = np.where(books_pt.index == book_name)[0][0]
    distances = books_similarity_score[book_index]
    recommended_books = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:5]
    data = []
    for i in recommended_books:
        item = []
        temp_df = books[books["Book-Title"] == books_pt.index[i[0]]].drop_duplicates("Book-Title")
        item.extend(temp_df["Book-Title"])
        item.extend(temp_df["Book-Author"])
        item.extend(temp_df["Image-URL-M"])
        data.append(item)
    return data


def MovieRecommend(movie_name):
    movie_index = movies[movies["title"]==movie_name].index[0]
    distances = movies_similarity_score[movie_index]
    recommended_movies_index_list = sorted(list(enumerate(distances)) ,reverse =True ,key = lambda x:x[1])[1:5]
    data : list = []
    for index , score in recommended_movies_index_list :
        items: dict = {}
        items['movie_title'] = movies.iloc[index].title
        items['poster_path'] = movies.iloc[index].poster_path #get_poster_path(movies.iloc[index].movie_id)
        data.append(items)
    return data     
        
        
