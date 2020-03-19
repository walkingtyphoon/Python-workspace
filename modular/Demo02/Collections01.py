from collections import namedtuple

Point = namedtuple("Point", ['x','y'])
# 可以转化为集合，然后可通过属性获取元素
p = Point(1, 2)
# 给集合赋值
print(p.x)
# 获取指定元素

