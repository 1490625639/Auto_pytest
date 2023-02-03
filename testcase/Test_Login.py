import requests

import os


def login():
    url = "https://app100.qiyuesuo.net/login"

    json = {"username": "10000000001",
            "password": "qiyuesuo#2020"}

    headers={

    }
    r = requests.post(url=url, json=json,headers=headers)
    r.encoding="utf-8"
    print(r.cookies)
    print(r.encoding)
    # with open("./a.html","w", encoding="utf-8") as f:
    #     f.write(response)
    print(r.status_code)


if __name__ == '__main__':
    login()

# file=open("./a.html","w")
