import os
import sys
from typing import List

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from client import Client

def get_post_stream(cli: Client, topic_id: int) -> List[int]:
    topic = cli.get_single_topic(topic_id)
    return topic.post_stream.stream

if __name__ == '__main__':
    cookies = ''
    with open('YOUR_COOKIES.txt', 'r') as f:
        cookies = f.read()
    cli = Client(cookies=cookies)

    testcases = [35167, 205204, 22873, 194085]

    for testcase in testcases:
        post_ids = get_post_stream(cli, testcase)
        topic = cli.get_single_topic(testcase)
        print(f'主题"{topic.title}"共有{len(post_ids)}条讨论')
    

    