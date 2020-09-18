from rotten_tomatoes_client import RottenTomatoesClient, TvBrowsingCategory
from pprint import pprint


def evalMovie(requestMovieName):
    try:
        result = RottenTomatoesClient.search(term=requestMovieName, limit=1)

        movieName = result.get("movies")[0].get("name")
        movieYear = result.get("movies")[0].get("year")
        movieRatingClass = result.get("movies")[0].get(
            "meterClass")  # certified_fresh
        movieRatingScore = result.get("movies")[0].get(
            "meterScore")  # certified_fresh

        retStr = "I found the movie '" + str(movieName) + "' from the year " + str(
            movieYear) + " . Its rating on Rotten Tomatoes is " + str(movieRatingScore)  # + " | " + str(movieRatingClass)
    except Exception as e:
        retStr = "Sorry, I don't know that movie"
    return retStr
