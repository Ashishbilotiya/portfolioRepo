
import numpy as np
from flask import render_template ,request ,Blueprint
from models import load_books , load_books_pt, load_books_similarity_score

books = None

book_page = Blueprint("BookRecommender",__name__)


def BookRecommenderFunc(book_name):
    books_pt = load_books_pt()
    books_similarity_score = load_books_similarity_score()
    book_index = None
    distances = None
    recommended_books = None    
    try :
        book_index = np.where(books_pt.index == book_name)[0][0]
        distances = books_similarity_score[book_index]
        recommended_books = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:5]
    except Exception as e :
        print("Error in finding recommendations:", e)
    data = []
    for i in recommended_books:
        item = []
        temp_df = books[books["Book-Title"] == books_pt.index[i[0]]].drop_duplicates("Book-Title")
        item.extend(temp_df["Book-Title"])
        item.extend(temp_df["Book-Author"])
        item.extend(temp_df["Image-URL-M"])
        data.append(item)
    return data


@book_page.route("/",methods=["POST","GET"])
def book_recommender_page():
    global books 
    books = load_books()
    book_titles = None
    try :
        book_titles = list(books["Book-Title"].drop_duplicates())
    except Exception as e :
        print("Error in fetching book titles:", e)
    success_code  =-1
    if request.method == "POST" :
        user_input = str(request.form.get("user_input"))
        if user_input :
            try:
                data= BookRecommenderFunc(user_input)
                success_code=1
                return render_template("book/BookRecommender.html",success=success_code,data=data,book_titles=book_titles,user_input=user_input)
            except:
                success_code=0
                return render_template("book/BookRecommender.html",success=success_code,book_titles=book_titles)
    return render_template("book/BookRecommender.html",success=success_code,book_titles=book_titles)
