import requests

data = requests.get("http://dl.ppt123.net/pptbj/51/20181115/5plurgisrd4.jpg")
# 获取连接的资源
target = data.content
# 建立连接
value = open("out/02.jpg", "wb")
# 创建输入的对象,使用二进制的形式写入
value.write(target)
# 写入对象
value.close()
# 关闭资源
