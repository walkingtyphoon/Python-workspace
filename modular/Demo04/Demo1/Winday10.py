import requests
from bs4 import BeautifulSoup

data = requests.get("https://localprod.pandateacher.com/python-manuscript/crawler-html/spder-men0.0.html")
# 获取链接中的数据
soup = BeautifulSoup(data.text, "html.parser")
# 使用 BeautifulSoup 解析网页数据
value = soup.find("div")
# 使用soup解析标签
values = soup.findAll("div")
# 获取所有的div标签
print(type(value))
# 输出soup的类型
print(value)
# 输出获取的值
print(type(values))
# 获取标签的类型
print(values)
# 获取所有的指定标签
