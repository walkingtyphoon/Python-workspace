value = 10.00
# print("将指定类型转化为int类型的数值", int(value))
string = "这是一个字符串"
# print("将目标转化为字符串：", str(value))
# print(type(string))
data = tuple(string)
# print("这是一个list转型后的", data)
pick = set(string)
# print("将目标转化为可变集合", pick)
introduce = [1, "大", 3, 'c', 5, 6]
# print(dict(pick=introduce))

# 结束位置插入元素
# introduce.append("这是结尾")

# 指定位置插入元素
# introduce.insert(0,"head")

# 列表扩充,参数为可迭代对象
# introduce.extend("这是扩充的")

# 删除指定位置的元素，无参数默认是删除结尾
# introduce.pop()
# introduce.pop(1)

# 删除指定元素
# introduce.remove('大')

# 修改列表
# introduce[0] = "head"
# print(introduce)

