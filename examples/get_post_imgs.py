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

    os.mkdir("good_stuff")
    dir = "good_stuff"

    imgs = post.get_imgs()
    for (i, img) in enumerate(imgs):
        save_path = os.path.join(dir, f'{i}.jpeg')
        cli.download_image(img.src, save_path)


    

    