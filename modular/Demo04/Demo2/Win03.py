import requests

data = requests.get("https://search.jd.com/Search?keyword=iPhone%20%E6%89%8B%E8%A1%A8&enc=utf-8&wq=iPhone%20shou%27biao&pvid=83f35be8f96f4dc7b2f9b62d32a48f4f")
# 使用requests对象获取网页信息
target = data.text
# 获取网页中的文本内容
print("网页中的文本内容为：", target)
# 打印网页中的信息

