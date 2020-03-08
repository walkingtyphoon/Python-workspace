import xlrd
workbook = xlrd.open_workbook("02.xlsx")
names = workbook.sheet_names()
nrows = wo
print(names)