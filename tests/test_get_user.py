import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from client import Client

def test_get_user():
    user_api_key = os.environ['USER_API_KEY']
    cli = Client(user_api_key=user_api_key)
    r = cli.get_user_by_username('addda')
    print(r.user.name)
    r = cli.get_user_by_username('凤凰院真凶')
    print(r.user.name)

def test_get_user_actions():
    user_api_key = os.environ['USER_API_KEY']
    cli = Client(user_api_key=user_api_key)
    r = cli.get_user_actions('addda')
    print(len(r.user_actions))
    r = cli.get_user_actions('凤凰院真凶')
    print(len(r.user_actions))