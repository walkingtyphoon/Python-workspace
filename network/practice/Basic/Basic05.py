# 一个景区根据游人的年龄收取不同价格的门票。请编写旅游人类，根据年龄段决定能够购
# 买的门票价格并输出，然后写出测试类测试该类（类的基本实现）


def buyCard(age):
    if age >= 18:
        print("需要支付的价格为：", 20)
    if age < 18:
        print("你可以免费参观，欢迎小朋友")


buyCard(10)