"""
对10个数进行排序。
"""


def sortNumber():
    value = []
    for i in range(10):
        temp = int(input("请输入你需要排序的数字"))
        value.append(temp)

    value.sort()

    print(value)


sortNumber()
