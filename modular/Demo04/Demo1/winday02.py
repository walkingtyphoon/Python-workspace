import csv

with open("../out/工作簿1.csv", newline='') as f:
    value = csv.reader(f)
    for row in value:
        print(row)

print("读取完毕")

with open("../out/工作簿1.csv", "a", newline='') as f:
    text = csv.writer(f)
    text.writerow([6, 'xiao wang', 22])

print("写入完毕")