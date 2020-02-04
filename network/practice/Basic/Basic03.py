arr = [1, 2, 3, 6, 9, 5, 7]
# 创建数组
n = len(arr)
# 获取数组的长度
for i in range(n):
    # 进行循环迭代
    for j in range(0, n - i - 1):
        # 循环迭代
        if arr[j] > arr[j + 1]:

            arr[j] = arr[j + 1]
            arr[j + 1] = arr[j]
            # 进行交换元素
print(arr)
