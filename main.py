# Import the required module

import csv , json , requests

"""

format --> https://api.themoviedb.org/3/movie/76341?api_key=<<api_key>> for movies
GET /movie/{movie_id}
GET /search/company

"""


def MovieDB_script():
    '''Main function to get movie info'''

    api_key = '1ff5e64828c4dd99b310dc81a34c56e0'
    base_url = 'https://api.themoviedb.org/3/'
    movie_search = 'Avatar'

    url = f"{base_url}search/company?api_key={api_key}&query={movie_search}"

    try:
        r = requests.get(url)
        r.raise_for_status
        # print(url)

    except Exception as e:
        print('Something Went Wrong ',e)


if __name__ == "__main__":

    MovieDB_script()
    print('Code Completed 🔥')