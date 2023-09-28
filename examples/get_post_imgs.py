import os
import sys
from typing import List

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from client import Client

if __name__ == '__main__':
    cookies = ''
    with open('YOUR_COOKIES.txt', 'r') as f:
        cookies = f.read()
    cli = Client(cookies=cookies)
    post = cli.retrieve_single_post(2110122)

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(post.cooked)
    imgs = soup.find_all('img')
    for img in imgs:
        src = img.get('src')
        # print(src)

        # You can deal with srcset as well ^_^.
        src_set = img.get('srcset')
        print(src_set)
    

    