import requests

URL_ID = 'https://hacker-news.firebaseio.com/v0/topstories.json'


def get_top_ids():
    get_ids = requests.get(URL_ID).json()[0:5]
    return get_ids
