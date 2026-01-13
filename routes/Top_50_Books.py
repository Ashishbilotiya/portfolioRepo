
from flask import render_template,Blueprint
from models.load_models import load_famous_books


top_books_page = Blueprint("top_books",__name__)

@top_books_page.route("/")
def show():
    famous_books = load_famous_books()
    book_title = None
    author = None
    image =  None
    votes = None
    rating = None
    try :
        book_title = famous_books["Book-Title"].to_list()
        author = famous_books["Book-Author"].to_list()
        image = famous_books["Image-URL-M"].to_list()
        votes = famous_books["Num-Rating"].to_list()
        rating = famous_books["Avg-Rating"].to_list()
    except Exception as e :
        print("Error in fetching top books data:", e)
    return render_template("book/TopBooks.html",
                           book_title=book_title,
                           author=author,
                           image=image,
                           votes=votes,
                           rating=rating,
                           )
    
