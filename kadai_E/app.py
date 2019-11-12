import time

import requests

from kadai_E.function import get_top_ids


def main():
    top_ids = get_top_ids()
    for top_id in top_ids:
        time.sleep(1)
        item = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{top_id}.json')
        print(item.json()['title'], item.json()['url'])


if __name__ == '__main__':
    main()
