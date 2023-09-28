import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils import generate_user_api_key
from client import Client


if __name__ == '__main__':
    result = generate_user_api_key('Shuiyuan Sample App')
    print(result.payload.key)
    cli = Client(user_api_key=result.payload.key)
    r = cli.list_user_badges('凤凰院真凶')
    print(r)
    
