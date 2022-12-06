import requests

import os


def login():
    url = "https://app100.qiyuesuo.net/login"

    data = {"username": "10000000001",
            "password": "qiyuesuo#2020"}


    r = requests.post(url=url, data=data)
    r.encoding="utf-8"
    response=r.text
    with open("./a.html","w", encoding="utf-8") as f:
        f.write(response)

# def login():
#     url = "https://www.baidu.com"
#     response = requests.post(url=url)
#     response.encoding = "utf-8"
#     ok = response.text
#
#     with open("./baidu.html", "w", encoding="utf-8") as f:
#         f.write(ok)


if __name__ == '__main__':
    login()

# file=open("./a.html","w")
