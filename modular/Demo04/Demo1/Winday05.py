import requests

data = requests.get("https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md")
# 读取三国演义的文件内容
pic = data.text
# 读取为字符串类型
value = open("三国演义.txt", 'a+')
# 创建一个指定的文本，并追加至文本
value.write(pic)
# 写入字符串到文件
value.close()
# 关闭资源
