"""
十六进制转化，从0到9，如果到10就是a，b,c,d,e,f,到达16时
就是10，17就是11，十八就是12
"""
value = 11
# 需要转化的目标数
target = 0xb
# 目标的期望值
print(f"{value}的期望值为{target},运行结果为：{hex(value)}")
