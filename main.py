import requests
import secrets

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def api_connect():
    return requests.get('https://imdb-api.com/API/Top250TVs/' + secrets.api_key)


def get_user_data(movie_id):
    return requests.get('https://imdb-api.com/en/API/UserRatings/' + secrets.api_key + '/' + movie_id)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    imdb_API = api_connect()
    print(imdb_API.status_code)
    print(imdb_API.text)
    print(imdb_API.headers)

    rank1_rated_show = get_user_data('tt5491994')
    print(rank1_rated_show.json())
    print(type(rank1_rated_show.json()))
    rank50_rated_show = get_user_data('tt2297757')
    print(rank50_rated_show.json())
    rank100_rated_show = get_user_data('tt0286486')
    print(rank100_rated_show.json())
    rank200_rated_show = get_user_data('tt1492966')
    print(rank200_rated_show.json())
    wheel_of_time_rating = get_user_data('tt7462410')
    print(wheel_of_time_rating.json())
