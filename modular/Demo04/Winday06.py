"""
题目要求：获取文章《HTTP状态响应码》全部内容，并且打印出全文内容。
获取数据：
    文本URL：
    https://localprod.pandateacher.com/python-manuscript/crawler-html/exercise/HTTP%E5%93%8D%E5%BA%94%E7%8A%B6%E6%80%81%E7%A0%81.md
    首先调用requests库，使用requests.get('URL')获取文件，返回的是Response对象。
    然后需要把Response对象用合适的数据形式返回。

存储数据：

    存储文件的三个步骤：打开文件，存储文件，关闭文件。
"""
import requests

data = requests.get("https://localprod.pandateacher.com/python-manuscript/crawler-html/exercise/HTTP%E5%93%8D%E5%BA"
                    "%94%E7%8A%B6%E6%80%81%E7%A0%81.md")
# 获取连接中的数据
target = data.text
# 获取目标的字符串形式
value = open("out/http状态响应码.md", 'a+', encoding="UTF-8")
# 创建写入的对象
value.write(target)
# 写入文本对象
value.close()
# 关闭资源
