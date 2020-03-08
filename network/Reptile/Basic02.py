from urllib import request

url = "http://quotes.toscrape.com/"
# 设置需要打开的链接
resp = request.urlopen(url)
# 使用请求函数打开链接
print(resp.read())
# 打印获取到的信息

