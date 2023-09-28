# Shuiyuan Client

![python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)

[水源社区](https://shuiyuan.sjtu.edu.cn/)是交大人日常必备的网站之一，社区里有非常丰富的资源和信息，开发一个便于调用接口的 client 比较有必要。

## 使用方法
+ 创建 client
    + 手动复制 cookies
        ```python
        cli = Client(cookies='COPY_YOUR_COOKIES_HERE')
        ```
    + 提供 jaccount 和密码，通过 selenium 自动获取 cookies
        ```python
        cli = Client(jaccount='YOUR_JACCOUNT', pwd='YOUR_PASSWORD')
        ```
    + 使用 User-Api-Key（见 https://shuiyuan.sjtu.edu.cn/t/topic/123808 ）
        ```python
        cli = Client(user_api_key='YOUR_USER_API_KEY')
        ```

## 使用例子
请见 examples 目录：
+ [statistic_emoji_usage.py](./examples/statistic_emoji_usage.py): 统计用户使用了哪些 emoji
+ [get_topic_posts.py](./examples/get_topic_posts.py): 获取某一主题下所有的 posts
+ [get_post_imgs.py](./examples/get_post_imgs.py): 获取某一 post 的所有图片链接（荣光楼🥵）
+ [get_user_posts.py](./examples//get_user_posts.py): 获取某一用户所有的 posts
+ [newest_recruit.py](./examples/newest_recruit.py): 获取最新的近半个月以来的招募信息
+ [user_api_key.py](./examples/user_api_key.py): 获取并使用 User-Api-Key
