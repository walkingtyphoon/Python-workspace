import sys
import os

filename = sys.argv[0]
if not os.path.isfile(filename):
    # 测试文件是否存在
    print("[-]" + filename + 'does not exit.')
    exit(0)
else:
    print("文件存在")

if os.access(filename, os.R_OK):
    # 测试用户是否有对应的权限
    print("用户拥有该文件的可读权限")

print(os.listdir("../../"))
# 列出当前目录
print(os.path.abspath("../../"))
# 获取当前的绝对路径
print("当前路径是否为目录：", os.path.isdir("../../"))
# 判断当前路径是否为目录
print("当前路径是否为文件：", os.path.isfile("../../"))
# 判断当前目录是否为文件
print(os.path.split("D:\File_System\Personal_Affairs\Python workspace\network\practice"))
# 把路径分割成路径名和basename，返回一个元组
