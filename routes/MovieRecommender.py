
from flask import render_template ,request ,Blueprint
from routes.utility_func import MovieRecommend 
from models import movies


movie_page = Blueprint("MovieRecommender",__name__)


@movie_page.route("/",methods=["POST","GET"])
def movie_recommender_page():
    titles = list(movies['title'])
    success_code = -1
    if request.method == "POST" :
        user_input = str(request.form.get("user_input"))
        if user_input :
            try :
                data = MovieRecommend(user_input)
                success_code= 1
                return render_template("movie/MovieRecommender.html",success=success_code,data = data,titles=titles,user_input=user_input)
            except:
                success_code = 0
                return render_template("movie/MovieRecommender.html",success = success_code,titles=titles)
    return render_template("movie/MovieRecommender.html",success=success_code,titles=titles)


