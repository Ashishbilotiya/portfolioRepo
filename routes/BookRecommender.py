
from flask import render_template ,request ,Blueprint
from routes.utility_func import BookRecommend
from models import books


book_page = Blueprint("BookRecommender",__name__)



@book_page.route("/",methods=["POST","GET"])
def book_recommender_page():
    book_titles = books["Book-Title"].drop_duplicates()
    success_code  =-1
    if request.method == "POST" :
        user_input = str(request.form.get("user_input"))
        if user_input :
            try:
                data= BookRecommend(user_input)
                success_code=1
                return render_template("book/BookRecommender.html",success=success_code,data=data,book_titles=book_titles,user_input=user_input)
            except:
                success_code=0
                return render_template("book/BookRecommender.html",success=success_code,book_titles=book_titles)
    return render_template("book/BookRecommender.html",success=success_code,book_titles=book_titles)
