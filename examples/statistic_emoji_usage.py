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
from exceptions import TooManyOperationsException

def unicode_str_to_emoji(unicode_str):
    unicode_list = unicode_str.split()
    emoji = ""
    for code_point in unicode_list:
        try:
            code_point_int = int(code_point, 16)
            emoji += chr(code_point_int)
        except ValueError:
            emoji += f"\\u{code_point}"
    return emoji

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
    # todo: fix failed
    while True:
        print(f'统计第{page_idx}页...')
        try: 
            r = cli.search(SearchQuery(username='凤凰院真凶'), page=page_idx)
        except TooManyOperationsException:
            time.sleep(5)
            continue

        if last_post_ids == r.grouped_search_result.post_ids:
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
                    code: str = emoji_code_map[matched_emoji]
                    code = code.replace('-', ' ')
                    emoji = unicode_str_to_emoji(code)
                    if emoji not in emoji_usage_statistic:
                        emoji_usage_statistic[emoji] = 0
                    emoji_usage_statistic[emoji] += 1
        print(emoji_usage_statistic)
        time.sleep(0.5)
    sorted_dict = sorted(emoji_usage_statistic.items(), key=lambda x: x[1], reverse=True)

    for key, value in sorted_dict:
        print(f"{key}: {value}")
    