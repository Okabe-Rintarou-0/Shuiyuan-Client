import os
import sys
import json
import re
import time

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
    db_json = ''
    with open('./db.json', 'r') as f:
        db_json = f.read()
    db = json.loads(db_json)
    emojis = db['emojis']
    emoji_code_map = {}
    
    for emoji in emojis:
        emoji_code_map[emoji['name']] = emoji['code']

    emoji_usage_statistic = {}

    last_post_ids = []
    page_idx = 1
    while True:
        print(page_idx)
        r = cli.search(SearchQuery(username='凤凰院真凶'), page=page_idx)
        if last_post_ids == r.grouped_search_result:
            break
        page_idx += 1
        last_post_ids = r.grouped_search_result.post_ids
        for post in r.posts:
            post_content = ''
            if post.is_full():
                post_content = post.blurb
            else:
                r2 = cli.retrieve_single_post(post.id)
                if r2 is not None:
                    post_content = r2.raw
            matched_emojis = re.findall(r':(\w+):', post_content)

            for matched_emoji in matched_emojis:
                if matched_emoji in emoji_code_map:
                    code = emoji_code_map[matched_emoji]
                    if '-' in code:
                        parts = code.split('-')
                        emoji = chr(int(parts[0], 16)) + chr(int(parts[1], 16))
                    else:
                        emoji = chr(int(code, 16))
                    if emoji not in emoji_usage_statistic:
                        emoji_usage_statistic[emoji] = 0
                    emoji_usage_statistic[emoji] += 1
        time.sleep(0.5)
    print(emoji_usage_statistic)
    