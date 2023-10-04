
import os
import sys
from typing import List

from bs4 import BeautifulSoup, Tag


currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from client import Client
from models.topic_post import Option

def plot_votes(title: str, options: List[Option], out_dir: str):
    import matplotlib.pyplot as plt
    plt.clf()
    candidates = []
    votes = []

    for option in options:
        candidates.append(option.html)
        votes.append(option.votes)

    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    plt.rcParams['axes.unicode_minus'] = False 
    plt.title(title)
    plt.bar(candidates, votes, color='skyblue')

    out_path = os.path.join(out_dir, f'{title}.png')
    plt.savefig(out_path)


if __name__ == '__main__':
    cookies = ''
    with open('YOUR_COOKIES.txt', 'r') as f:
        cookies = f.read()

    cli = Client(cookies=cookies)
    post_id = 1412235
    post = cli.retrieve_single_post(post_id)
    topic_id = post.topic_id
    posts = cli.get_topic_posts(topic_id, post_ids=[post_id])

    if not os.path.exists('votes'):
        os.mkdir("votes")

    for post in posts.post_stream.posts:
        soup = BeautifulSoup(post.cooked, 'html.parser')
        poll_elements: List[Tag] = soup.find_all("div", attrs={"class": "poll"})

        vote_title_map = {}
        for poll_element in poll_elements:
            title = poll_element.find_previous("p").get_text()
            poll_name = poll_element.get("data-poll-name")
            vote_title_map[poll_name] = title

        for poll in post.polls:
            plot_votes(vote_title_map[poll.name], poll.options, "votes")
            

        
                