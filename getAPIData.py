import requests
import secrets
import sys


def get_movie_and_show_data() -> list[list[dict]]:
    top_250_tv_query = f"https://imdb-api.com/en/API/Top250TVs/{secrets.secret_key}"
    top_250_movie_query = f"https://imdb-api.com/en/API/Top250Movies/{secrets.secret_key}"
    popular_tv_query = f"https://imdb-api.com/en/API/MostPopularTVs/{secrets.secret_key}"
    popular_movie_query = f"https://imdb-api.com/en/API/MostPopularMovies/{secrets.secret_key}"
    top_tv_response = requests.get(top_250_tv_query)
    top_movie_response = requests.get(top_250_movie_query)
    popular_tv_response = requests.get(popular_tv_query)
    popular_movie_response = requests.get(popular_movie_query)
    if top_tv_response.status_code != 200 or top_movie_response.status_code != 200 or \
            popular_tv_response.status_code != 200 or popular_movie_response.status_code != 200:
        print("Failed to get data")
        sys.exit(-1)
    top_tv_json = top_tv_response.json()
    top_movie_json = top_movie_response.json()
    popular_tv_json = popular_tv_response.json()
    popular_movie_json = popular_movie_response.json()
    query_data = [top_tv_json['items'], top_movie_json['items'], popular_tv_json['items'], popular_movie_json['items']]
    return query_data


def get_ratings(top_show_data: list[dict]) -> list[dict]:
    results = []
    api_queries = []
    base_query = f"https://imdb-api.com/en/API/UserRatings/{secrets.secret_key}/"
    wheel_of_time_query = f"{base_query}tt7462410"
    api_queries.append(wheel_of_time_query)
    first_query = f"{base_query}{top_show_data[0]['id']}"
    api_queries.append(first_query)
    fifty_query = f"{base_query}{top_show_data[49]['id']}"
    api_queries.append(fifty_query)
    hundred_query = f"{base_query}{top_show_data[99]['id']}"
    api_queries.append(hundred_query)
    two_hundred = f"{base_query}{top_show_data[199]['id']}"
    api_queries.append(two_hundred)
    for query in api_queries:
        response = requests.get(query)
        if response.status_code != 200:  # if we don't get an ok response we have trouble, skip it
            print(f"Failed to get data, response code:{response.status_code} and error message: {response.reason} ")
            continue
        rating_data = response.json()
        results.append(rating_data)
    return results
