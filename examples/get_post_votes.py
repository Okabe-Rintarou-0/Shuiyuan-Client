
import os
import sys


currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from client import Client


if __name__ == '__main__':
    cookies = ''
    with open('YOUR_COOKIES.txt', 'r') as f:
        cookies = f.read()

    cli = Client(cookies=cookies)
    posts = cli.get_topic_posts(134841)
    for post in posts.post_stream.posts:
        print(post.polls)
    # topic = cli.get_single_topic(134841)
    # posts = topic.post_stream.stream

    # target = posts[0]
    # print(target)

    # post = cli.retrieve_single_post(target)
    # print(post.cooked)
