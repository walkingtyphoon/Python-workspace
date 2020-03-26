import requests

data = requests.get(
    "https://desk-fd.zol-img.com.cn/t_s1920x1080c5/g2/M00/09/0C/ChMlWl5UfAeIF7oVAAMW9Vo1S_gAANcvAJ4nKkAAxcN568.jpg")
# 发出请求并将其保存到结果中
pic = data.content
# 请求内容以二进制的形式返回
photo = open("out/01.jpg", 'wb')
# 创建写入的对象，w写入，b使用二进制
photo.write(pic)
# 写入对象
photo.close()
# 关闭资源

