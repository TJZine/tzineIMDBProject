import requests
import secrets


def api_connect():
    return requests.get('https://imdb-api.com/API/Top250TVs/' + secrets.api_key)


def get_user_data(movie_id):
    return requests.get('https://imdb-api.com/en/API/UserRatings/' + secrets.api_key + '/' + movie_id)


def write_to_file(top_shows_list):
    with open("output/shows.txt", "a") as writeFile:
        writeFile.write(top_shows_list)  # open shows.txt to write to file


if __name__ == '__main__':
    eraseFile = open("output/shows.txt", "w")  # erases any previous text in the file
    eraseFile.close()

    imdb_API = api_connect()
    print(imdb_API.status_code)

    write_to_file("User Ratings:" + "\n")
    rank1_rated_show = get_user_data('tt5491994')
    write_to_file(str(rank1_rated_show.json()) + "\n")
    print(rank1_rated_show.json())
    rank50_rated_show = get_user_data('tt2297757')
    write_to_file(str(rank50_rated_show.json()) + "\n")
    print(rank50_rated_show.json())
    rank100_rated_show = get_user_data('tt0286486')
    write_to_file(str(rank100_rated_show.json()) + "\n")
    print(rank100_rated_show.json())
    rank200_rated_show = get_user_data('tt1492966')
    write_to_file(str(rank200_rated_show.json()) + "\n")
    print(rank200_rated_show.json())
    wheel_of_time_rating = get_user_data('tt7462410')
    write_to_file(str(wheel_of_time_rating.json()) + "\n")
    print(wheel_of_time_rating.json())
    write_to_file("Top 250 Shows:" + "\n")
    text_value = imdb_API.text
    value_list = text_value.split('},{')
    value_list[0] = value_list[0][11:]
    print(value_list[0])
    for n in value_list:
        print(n)
        write_to_file(n + "\n")
