
from flask import render_template ,request ,Blueprint
from portfolioRepo.models.load_models import load_movies, load_movies_similarity_score

movies = None

movie_page = Blueprint("MovieRecommender",__name__)


def MovieRecommenderFunc(movie_name):
    movies_similarity_score = load_movies_similarity_score()
    movie_index = None
    distances = None
    recommended_movies_index_list = None    
    try :
        movie_index = movies[movies["title"]==movie_name].index[0]
        distances = movies_similarity_score[movie_index]
        recommended_movies_index_list = sorted(list(enumerate(distances)) ,reverse =True ,key = lambda x:x[1])[1:5]
    except Exception as e :
        print("Error in finding recommendations:", e)
    data : list = []
    for index , score in recommended_movies_index_list :
        items: dict = {}
        items['movie_title'] = movies.iloc[index].title
        items['poster_path'] = movies.iloc[index].poster_path #get_poster_path(movies.iloc[index].movie_id)
        data.append(items)
    return data     
        

@movie_page.route("/",methods=["POST","GET"])
def movie_recommender_page():
    global movies
    movies = load_movies()
    titles = None
    try :
        titles = list(movies['title'].drop_duplicates())
    except Exception as e :
        print("Error in fetching movie titles:", e)
    success_code = -1
    if request.method == "POST" :
        user_input = str(request.form.get("user_input"))
        if user_input :
            try :
                data = MovieRecommenderFunc(user_input)
                success_code= 1
                return render_template("movie/MovieRecommender.html",success=success_code,data = data,titles=titles,user_input=user_input)
            except:
                success_code = 0
                return render_template("movie/MovieRecommender.html",success = success_code,titles=titles)
    return render_template("movie/MovieRecommender.html",success=success_code,titles=titles)


