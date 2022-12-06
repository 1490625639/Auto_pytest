import requests

# r=requests.get(url="https://www.baidu.com/").content
r = requests.get(url="https://www.baidu.com/")
s = r.content
print(s, end="\n")
print("内容", r.content)
print("状态码", r.status_code)
print("请求头", r.headers)
print("url", r.url)
# print("json",r.json())
print("cookies ", r.cookies)
print("text", r.text)
