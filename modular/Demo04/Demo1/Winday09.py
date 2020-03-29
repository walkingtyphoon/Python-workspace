import requests
from bs4 import BeautifulSoup

data = requests.get("https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html")
# 使用requests对象获取数据
soup = BeautifulSoup(data.text, "html.parser")
# 使用解析器解析对象
print(type(soup))
# 获取soup对象的类型
print("soup 对象数据为：", soup)
# 打印 soup 对象解析的数据

