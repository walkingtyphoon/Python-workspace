"""
输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
"""


def countString(string):
    dictsort = {}
    # 创建空字典
    for i in string:
        # 遍历字符串
        if i in dictsort:
            dictsort[i] = dictsort[i] + 1
        else:
            dictsort[i] = 1


countString("abbccc")
