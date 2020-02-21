"""
有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
"""


def insertNumbers(value):
    arrays = [1, 3, 4, 5, 6, 8, 10]
    for i in range(len(arrays)):
        if arrays[i] < int(value) < arrays[i + 1]:
            # 说实话我没看懂
            arrays.insert(i + 1, value)
    print(arrays)


insertNumbers(2)
