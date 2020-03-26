import requests
data = requests.get("http://quotes.toscrape.com/")
print(type(data))

print("获取链接的状态码：", data.status_code)

