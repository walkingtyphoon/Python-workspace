from urllib import request
from urllib import parse

head = request.urlopen("http://www.baidu.com")
print("读取数据", head.read())
print("按行读取数据", head.readline())
print("多行读取数据", head.readlines())
print("读取返回的信息：", head.getcode())
request.urlretrieve(
    "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1581932221441&di"
    "=09a3b2baa29cfe07c21337a30e5c4080&imgtype=jpg&src=http%3A%2F%2Fwww.rfuchina.com%2Fuploadfile%2F2019%2F0417"
    "%2F20190417091923688.jpg",
    "01/01.jpg")
# 将指定文件保存到本地

params = {"name": "张三", "age": "18", "greet": "hello world"}
result = parse.urlencode(params)
print(result)
# 将字符进行编码

