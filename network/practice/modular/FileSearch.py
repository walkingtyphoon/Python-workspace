import os


def searchFile(path):
    value = os.walk(path)
    temp = input("请输入你需要检索的参数：")
    for i, j, k in value:
        if str(k).endswith(temp):
            print(k)


def main():
    searchFile("D:/")


main()
