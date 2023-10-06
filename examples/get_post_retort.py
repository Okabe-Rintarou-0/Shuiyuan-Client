import json
import os
import sys
from typing import List

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from client import Client

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

    with open('./db.json', 'r') as f:
        db_json = f.read()
        db = json.loads(db_json)
        emojis = db['emojis']
        emoji_code_map = {}
    
    for emoji in emojis:
        emoji_code_map[emoji['name']] = emoji['code']

    post = cli.retrieve_single_post(2404119)
    for retort in post.retorts:
        usernames = retort['usernames']
        emoji = retort['emoji']
        if emoji in emoji_code_map:
            emoji = unicode_str_to_emoji(emoji_code_map[emoji])
        
        print(f'{usernames[0]}等{len(usernames)}人贴了{emoji}')
            



    

    