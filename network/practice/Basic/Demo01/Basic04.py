# 实现会员注册，要求用户名长度不小于 3，密码长度不小于 6，注册时两次输入密码必
# 须相同 （字符串）

user_id = input("请输入你的账号：")
password = input("请输入你的密码：")
second_password = input("请再次输入你的密码：")
if len(user_id) > 6 and len(password) > 6 and len(second_password) > 6:
    if password == second_password:
        print("登陆成功,欢迎你,", user_id)
    else:
        print("你输入的两次密码，不相符合")
else:
    print("你输入的字符长度有误")
