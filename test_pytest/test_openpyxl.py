import openpyxl

# ��ȡ������
book = openpyxl.load_workbook('../data/test.xlsx')

# ��ȡ������
sheet = book.active

# ��ȡ������Ԫ��
cell_a1 = sheet['A1']
cell_a3 = sheet.cell(column=1, row=3)

# ��ȡ���������Ԫ��
cells = sheet['A1':'A3']

# ��ȥ��Ԫ���ֵ
cell_a1.value
