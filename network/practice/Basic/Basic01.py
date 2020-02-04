"""
编写一个 Java 程序，用 if-else 语句判断某年份是否为闰年。(分支)
闰年是公历中的名词。闰年分为普通闰年和世纪闰年。
普通闰年:公历年份是4的倍数的，且不是100的倍数，为闰年。（如2004年就是闰年）；
世纪闰年:公历年份是整百数的，必须是400的倍数才是世纪闰年（如1900年不是世纪闰年，2000年是世纪闰年）；
"""


def judge_leap_Year(year):
    if year % 4 == 0 and year % 100 != 0:
        print(year, "是闰年")
    elif year % 400 == 0:
        print(year, "是闰年")
    else:
        print("不是闰年")


judge_leap_Year(2100)
