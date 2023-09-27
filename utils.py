from datetime import datetime
import base64
import json
import secrets
import urllib.parse
import uuid
import webbrowser
from collections.abc import Iterable
from dataclasses import dataclass

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa

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


SITE_URL_BASE = 'https://shuiyuan.sjtu.edu.cn'
ALL_SCOPES = [
    'read',
    'write',
    'message_bus',
    'push',
    'one_time_password',
    'notifications',
    'session_info',
    'bookmarks_calendar',
    'user_status',
]
DEFAULT_SCOPES = ['read']


@dataclass
class UserApiKeyPayload:
    key: str
    nonce: str
    push: bool
    api: int


@dataclass
class UserApiKeyRequestResult:
    client_id: str
    payload: UserApiKeyPayload

# author: https://shuiyuan.sjtu.edu.cn/t/topic/123808
def generate_user_api_key(
    application_name: str, *,
    client_id: str | None = None,
    scopes: Iterable[str] | None = None,
) -> UserApiKeyRequestResult:
    # Generate RSA key pair.
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096,
    )
    public_key = private_key.public_key()
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    ).decode('ascii')

    # Generate a random client ID if not provided.
    client_id_to_use = str(uuid.uuid4()) if client_id is None else client_id
    nonce = secrets.token_urlsafe(32)

    # Validate scopes.
    scopes_list = DEFAULT_SCOPES if scopes is None else list(scopes)
    if not set(scopes_list) <= set(ALL_SCOPES):
        raise ValueError('Invalid scopes')

    # Build request URL and open in browser.
    params_dict: dict[str, str] = {
        'application_name': application_name,
        'client_id': client_id_to_use,
        'scopes': ','.join(scopes_list),
        'public_key': public_key_pem,
        'nonce': nonce,
    }
    params_str = '&'.join(
        f'{k}={urllib.parse.quote(v)}' for k, v in params_dict.items())
    webbrowser.open(f'{SITE_URL_BASE}/user-api-key/new?{params_str}')

    # Receive, decrypt and check response payload from server.
    enc_payload = input('Paste the response payload here: ')
    dec_payload = UserApiKeyPayload(**json.loads(private_key.decrypt(
        base64.b64decode(enc_payload),
        padding.PKCS1v15(),
    )))
    if dec_payload.nonce != nonce:
        raise ValueError('Nonce mismatch')

    # Return client ID and response payload.
    return UserApiKeyRequestResult(
        client_id=client_id_to_use,
        payload=dec_payload,
    )
