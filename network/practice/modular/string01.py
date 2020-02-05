banner = "FreeFloat FTP Server"
print(banner.upper())
# 将字符串转化为大写
print(banner.lower())
# 将字符串转化为小写
print(banner.find("FTP"))
# 查看是否包含指定的字符串
portlist = []
# 创建空的列表
portlist.append(21)
portlist.append(80)
portlist.append(22)
portlist.append(22)
# 添加列表 只能添加同类型的数据，可以重复
portlist.sort()
# 列表进行排序
print(portlist)
print(portlist.index(80))
# 返回数据对应的索引
portlist.remove(22)
# 删除对应的数据
print(portlist)
print("列表的长度为:", len(portlist))