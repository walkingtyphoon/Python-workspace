import csv

with open("../out/工作簿2.csv", 'a', newline='') as f:
    # 写入表格 a 为追加
    writers = csv.writer(f)
    # 写入文件
    header = ['大数据成绩统计表']
    writers.writerow(header)
    message = ['id', 'name', 'age']
    writers.writerow(message)

print("写入完毕，请查看")

