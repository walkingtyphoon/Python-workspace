import requests
from bs4 import BeautifulSoup

data = requests.get("https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html")
# 获取网页链接
target = data.text
# 获取网页的源代码
soup = BeautifulSoup(target,'html.parser')
# 使用html解析器，解析数据
print("程序响应码：", data.status_code)
# 返回程序响应码
print(" 解析的数据： ", target)
# 获取网页的源代码
print(" soup = ", soup)

