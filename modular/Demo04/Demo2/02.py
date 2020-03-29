import pymysql

try:
    connection = pymysql.connect()

    cur = connection.cursor()
    # 创建一个游标对象
    for i in cur.execute("SELECT VERSION()"):
        print(i)
    connection.close()
except:
    print("发生了异常")
