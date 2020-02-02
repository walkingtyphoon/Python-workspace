"""
置的sys模块提供访问和维护python解释器的能力。
这包括了提示信息，版本，整数的最大值，可用模块，
路径钩子，标准错误，标准输入输出的定位和解释器
调用的命令行参数。你能够在python的在线模块文档
上找到更多与此相关的信
"""
import sys

# if len(sys.argv) <= 2:
#     filename = sys.argv[0].split("/")[-1]
#     # 将当前的对象转化，切割出最后一个文件
#     print("[+]Reading Vulnerabilities From:" + str(filename))
"""
python range() 函数可创建一个整数列表，一般用在 for 循环中。
函数语法

range(start, stop[, step])

参数说明：

    start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
    stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
    step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
"""

# 退出程序
# for i in range(100):
#     if i == 50:
#         sys.exit(0)
#     print(str(i))

# 获python解释器的版本信息
# print(sys.version)

# 获取int的最大值 9223372036854775807
# print(sys.maxsize)

# 获取模块的搜索路径 返回的是一个列表
# sp = sys.path
# print(type(sp))

# 返回操作平台的名称
# print(sys.platform)

