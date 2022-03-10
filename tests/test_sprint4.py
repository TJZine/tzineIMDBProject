import test_sprint3


def top_250_dict_test() -> list[dict]:
    top_250_dict = [
        {'id': 'tt0537377',  'title': 'test_show_title3',
         'fullTitle': 'full_show_title (2000)', 'year': '2000',
         'image': 'www.testURL.com', 'crew': 'actor 1, actor 2, actor 3',
         'imDbRating': 6.7, 'imDbRatingCount': 22222},
        {'id': 'tt2278757', 'title': 'show_title_2',
         'fullTitle': 'full_show_title_2 (2011)', 'year': '2011',
         'image': 'www.testURL2.com', 'crew': 'actor 1, actor 2, actor 3',
         'imDbRating': 6.5, 'imDbRatingCount': 17052},
        {'id': 'tt2255557', 'title': 'show_title_33',
         'fullTitle': 'full_show_title_3 (2012)', 'year': '2012',
         'image': 'www.testURL3.com', 'crew': 'actor 1, actor 2, actor 3',
         'imDbRating': 6.4, 'imDbRatingCount': 18073},
        {'id': 'tt2356557', 'title': 'show_title_4',
         'fullTitle': 'full_show_title_4 (2007)', 'year': '2007',
         'image': 'www.testURL5.com', 'crew': 'actor 1, actor 2, actor 3',
         'imDbRating': 7.2, 'imDbRatingCount': 15012},
        {'id': 'tt2414525', 'title': 'show_title_37',
         'fullTitle': 'full_show_title_7 (1999)', 'year': '1999',
         'image': 'www.testURL2.com', 'crew': 'actor 1, actor 2, actor 3',
         'imDbRating': 6.8, 'imDbRatingCount': 10045},
        {'id': 'tt2446524', 'title': 'show_title_29',
         'fullTitle': 'full_show_title_9 (2022)', 'year': '2022',
         'image': 'www.testURL2.com', 'crew': 'actor 1, actor 2, actor 3',
         'imDbRating': 7.4, 'imDbRatingCount': 4511}
    ]
    return top_250_dict


def test_cross_ref():
    most_pop_dict = test_sprint3.popular_dict_test()
    top_250_dict = top_250_dict_test()
