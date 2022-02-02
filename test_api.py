# input show

def get_user_data(movie_id):
    return requests.get('https://imdb-api.com/en/API/UserRatings/' + secrets.api_key + '/' + movie_id)

def get_show_test():
    show_response = get_user_data('tt8420184')
    response_content = show_response.json()
    assert response_content["rank"] == "16"
