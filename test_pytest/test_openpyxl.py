import openpyxl

# 获取工作簿
book = openpyxl.load_workbook('../data/test.xlsx')

# 读取工作表
sheet = book.active

# 读取单个单元格
cell_a1 = sheet['A1']
cell_a3 = sheet.cell(column=1, row=3)

# 读取多个连续单元格
cells = sheet['A1':'A3']

# 回去单元格的值
cell_a1.value
