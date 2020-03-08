from urllib import parse

url = "https://www.baidu.com/s?wd=%E5%A4%A7%E6%95%B0%E6%8D%AE&rsv_spt=1&rsv_iqid=0xcfe8272000019d00&issp=1&f=8&rsv_bp" \
      "=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=tb&rsv_sug3=9&rsv_sug1=6&rsv_sug7=100&rsv_sug2=0" \
      "&inputT=2063&rsv_sug4=2999 "
message = parse.urlparse(url)
# 解析url
mes = parse.urlsplit(url)
# 切割链接
print("使用urlparse",message)
# 使用后可以获取到参数
print("使用urlsplit",mes)
# 使用后获取不到参数
print("scheme",message.scheme)
print("netloc",message.netloc)
