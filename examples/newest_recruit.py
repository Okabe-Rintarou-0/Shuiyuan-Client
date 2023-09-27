from datetime import datetime, timedelta
import pandas as pd

import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from client import Client
from constants import base_url
from models.search import SearchQuery, SearchQueryOrder, SearchQueryStatus


if __name__ == '__main__':
    cookies = ''
    with open('YOUR_COOKIES.txt', 'r') as f:
        cookies = f.read()
    cli = Client(cookies=cookies)

    out_data = {
        '标题': [],
        '发布日期': [],
        'url': []
    }
    current_date = datetime.now()
    fifteen_days_ago = current_date - timedelta(days=15)
    fifteen_days_ago = fifteen_days_ago.strftime("%Y-%m-%d")

    data = cli.search(SearchQuery('招募', order=SearchQueryOrder.LATEST,
                      after=fifteen_days_ago, status=SearchQueryStatus.OPEN))

    for topic in data.topics:
        created_at = topic.created_at
        created_at = created_at.strftime("%Y年%m月%d日 %H时%M分%S秒")

        url = f'{base_url}/t/topic/{id}'
        out_data['标题'].append(topic.title)
        out_data['url'].append(url)
        out_data['发布日期'].append(created_at)

    out_data = pd.DataFrame(out_data)
    out_data['raw_url'] = out_data['url']
    out_data['url'] = out_data['url'].apply(
        lambda x: f'=HYPERLINK("{x}", "{x}")')
    out_data.to_excel('./latest.xlsx')
