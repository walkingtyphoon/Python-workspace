import requests
from bs4 import BeautifulSoup

data = requests.get("http://books.toscrape.com/")
# 获取链接
soup = BeautifulSoup(data.text, "html.parser")
# 解析数据
items = soup.find(class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
# 获取所有的标签数据
print("程序响应码：", data.status_code)
for i in items:
    print(i.findAll("h3").text)

