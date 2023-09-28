import time
from typing import Any, Optional, Union
from urllib.parse import urlencode
import requests
from exceptions import ResponseDataFormatErrorException, TooManyOperationsException

from models.search import SearchQuery, SearchResult
from models.user import UserBadgesInfo, UserInfo
from models.post import Post

from selenium import webdriver

from utils import pack_query
from constants import search_url, user_badges_url, not_found_error, post_url, base_url, too_many_operations_warning
from selenium.webdriver.common.by import By
import pytesseract


class Client():
    def __init__(self, cookies: str = '', user_api_key: str = '', jaccount: str = '', pwd: str = '') -> None:
        if user_api_key != '':
            self.headers = {
                'User-Api-Key': user_api_key
            }
            return

        if cookies == '':
            cookies = self._get_cookies(jaccount, pwd)
            if cookies is None:
                raise RuntimeError(
                    'Please provide correct jaccount and password!')

        self.headers = {
            'Cookie': cookies,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    @staticmethod
    def _get_supported_webdriver() -> Union[None, webdriver.Chrome, webdriver.Edge, webdriver.Safari]:
        try:
            return webdriver.Chrome()
        except:
            pass

        try:
            return webdriver.Edge()
        except:
            pass

        try:
            return webdriver.Safari()
        except:
            pass
        return None

    @staticmethod
    def _get_cookies(jaccount: str, password: str) -> Optional[str]:
        driver = Client._get_supported_webdriver()
        if driver is None:
            raise RuntimeError('No available web driver!')

        driver.implicitly_wait(10)
        driver.get(base_url)

        max_retries = 5
        retry_cnt = 0
        while retry_cnt < max_retries:
            driver.find_element(By.ID, "user").send_keys(jaccount)
            driver.find_element(By.ID, "pass").send_keys(password)

            captcha = driver.find_element(By.ID, "captcha-img")
            with open('captcha.png', 'wb') as f:
                f.write(captcha.screenshot_as_png)
            captcha = pytesseract.image_to_string(
                'captcha.png', lang='eng', config='--psm 7')

            driver.find_element(By.ID, "captcha").send_keys(captcha)

            time.sleep(0.5)

            if driver.current_url.find(base_url) != -1:
                break

            retry_cnt += 1

        if retry_cnt == max_retries:
            return None

        cookies = driver.get_cookies()
        cookies = '; '.join(
            [f"{cookie['name']}={cookie['value']}" for cookie in cookies])
        return cookies

    def _get_request(self, url: str):
        return requests.get(url=url, headers=self.headers)
    
    def _check_error(self, data: Any) -> bool:
        if 'failed' in data and 'message' in data:
            if data['message'] == too_many_operations_warning:
                raise TooManyOperationsException() 

            raise RuntimeError(data['message'])
        
        if 'errors' in data and not_found_error in data['errors']:
            return False
        return True

    def search(self, query: SearchQuery, page: int = 1) -> SearchResult:
        q = pack_query(query)
        params = {
            'q': q,
            'page': page
        }
        url = search_url + urlencode(params)
        r = self._get_request(url)
        try:
            data = r.json()
            self._check_error(data)
            return SearchResult.from_dict(data)
        except TooManyOperationsException as e:
            raise e
        except:
            print(r.text)
            raise ResponseDataFormatErrorException()
        
    def get_user_by_username(self, username: str) -> Optional[UserInfo]:
        url = f'{base_url}/u/{username}.json'
        r = self._get_request(url)
        try:
            data = r.json()
            if not self._check_error(data):
                return None
            return UserInfo.from_dict(data)
        except TooManyOperationsException as e:
            raise e
        except:
            print(r.text)
            raise ResponseDataFormatErrorException()

    def list_user_badges(self, username: str) -> Optional[UserBadgesInfo]:
        url = user_badges_url + f'/{username}.json'
        r = self._get_request(url)
        try:
            data = r.json()
            if not self._check_error(data):
                return None
            return UserBadgesInfo.from_dict(data)
        except TooManyOperationsException as e:
            raise e
        except:
            raise ResponseDataFormatErrorException()

    def retrieve_single_post(self, id: str) -> Optional[Post]:
        url = post_url + f'/{id}.json'
        r = self._get_request(url)
        try:
            data = r.json()
            if not self._check_error(data):
                return None
            return Post.from_dict(data)
        except TooManyOperationsException as e:
            raise e
        except:
            raise ResponseDataFormatErrorException()

