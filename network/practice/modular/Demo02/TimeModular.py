import time
import calendar

ticks = time.time()
# 获取当前的毫秒值
print("当前的时间戳：", ticks)


localtime = time.localtime()
# 获取当前的格式化时间
print(localtime)

asctime = time.asctime(localtime)
# 获取当前的格式化后的字符串
print(asctime)

strtime = time.strftime("%Y-%d-%d %H:%M:%S", localtime)
# 转化为可以看懂的字符串
print(strtime)

cl = calendar.month(2020,2)
# 获取指定月份的日历
print(cl)