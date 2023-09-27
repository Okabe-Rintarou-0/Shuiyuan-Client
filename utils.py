from datetime import datetime

from models.search import SearchQuery


def is_valid_date(date_str: str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False
    
def pack_query(q: SearchQuery) -> str:
    terms = []
    if len(q.term) > 0:
        terms.append(q.term)
    if len(q.username) > 0:
        terms.append(f'@{q.username}')
    if len(q.category) > 0:
        terms.append(f'category:{q.category}')
    if len(q.before) > 0 and is_valid_date(q.before):
        terms.append(f'before:{q.before}')
    if len(q.after) > 0 and is_valid_date(q.after):
        terms.append(f'after:{q.after}')
    if len(q.order.value) > 0:
        terms.append(f'order:{q.order.value}')
    if len(q.status.value) > 0:
        terms.append(f'status:{q.status.value}')
    if len(q.in_whats) > 0:
        for in_what in q.in_whats:
            terms.append(f'in:{in_what.value}')
    return '  '.join(terms)

