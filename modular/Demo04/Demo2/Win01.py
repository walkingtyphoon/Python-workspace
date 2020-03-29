import requests
from bs4 import BeautifulSoup

"""
爬取网页中的三本书的书名、链接、和书籍介绍。
"""
data = requests.get("https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html")
# 获取网页数据
soup = BeautifulSoup(data.text, "html.parser")
# 解析数据
items = soup.findAll(class_="books")
# 获取所有的书籍信息
for i in items:
    print("提取标签中的标签:", i.find(class_="title").text)
    # 获取指定属性的值
    print("提取标签中的标签:", i.find(class_="info").text)



