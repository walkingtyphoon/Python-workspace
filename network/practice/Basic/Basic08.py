# while循环
# for i in range(10):
#    print(i)

# while循环
# n = 1
# while n < 10:
#     print(n)
#     n += 1
# else:
#     print("loop end")
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(f'{i}*{j}={i*j}', end=" ")
#     print()


# for循环嵌套
# i = 1
#
# while i<10:
#     j = 1
#     while j<i+1:
#         print(f'{j}*{i}={i*j}', end=" ")
#         j +=1
#     print()
#     i+=1

# for循环和while循环嵌套
# n = 1
# while n < 10:
#     for i in range(1, n + 1):
#         print(f"{i}*{n}={n * i}", end=" ")
#     n += 1
#     print()

# 测试常用语句
# while True:
# s = input("输入0结束：")
# if s == '0':
# continue
# break 如果符合要求就结束程序
#     print("你输入的是：", s)

# for循环的其他用法
# for i in [1, 2, 3, 4, 5, 6]:
#     if i == 3:
#         continue
#     print(i)

# 制作猜数字的游戏
# import random
#
# value = random.randint(1, 200)
# while True:
#     n = int(input("请输入你猜的数字："))
#     if n > value:
#         print("猜的数字大了")
#     elif n < value:
#         print("猜的数字小了")
#     else:
#         print("你猜对了")
#         break

# 字符串的序列
# string = "这是测试的"
# print(string[1:4:2])
# 第三个参数为步长,每两个取一个
# print(string[:])
# 取出所有

# 格式化输出
string1="小米"
string2="华为"
print("{}对{}说：hello world".format(string1,string2))
print(f"{string1}对{string2}说：hello world")