import requests
# 导入请求包
data = requests.get("http://quotes.toscrape.com/")
# 使用requests对象获取链接中的数据
print(type(data))
# 获取数据的类型
print("获取链接的状态码：", data.status_code)
# 输出返回的状态码

