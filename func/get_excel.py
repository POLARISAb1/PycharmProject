# coding=utf-8
import openpyxl


def get_excel():
    book = openpyxl.load_workbook('../data/test.xlsx')
    sheet = book.active
    values = []
    for raw in sheet:
        line = []
        for cell in raw:
            line.append(cell.value)
        values.append(line)
    print(values)
    return values

