import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from client import Client
from models.search import SearchQuery


if __name__ == '__main__':
    cookies = ''
    with open('YOUR_COOKIES.txt', 'r') as f:
        cookies = f.read()
    cli = Client(cookies=cookies)
    r = cli.search(SearchQuery(username='凤凰院真凶'), page=1)
    for post in r.posts:
        if post.is_full():
            print(post.blurb)
        else:
            r2 = cli.retrieve_single_post(post.id)
            if r2 is not None:
                print(r2.raw)

    