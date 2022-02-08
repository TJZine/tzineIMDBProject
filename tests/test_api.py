import requests
import secrets
import imdbDB


def test_connect(movie_id):
    return requests.get('https://imdb-api.com/en/API/UserRatings/' + secrets.api_key + '/' + movie_id)


def test_get_show():
    show_response = test_connect('tt8420184')
    response_content = show_response.json()
    assert response_content["rank"] == "16"
