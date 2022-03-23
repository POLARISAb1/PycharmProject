# coding=utf-8

# 读取csv文件内容
import csv


def get_csv():
    with open('../data/params.csv', 'r') as file:
        csv_file = csv.reader(file)
        data_list = []
        for row in csv_file:
            tu_row = tuple(row)
            # print(tu_row)
            data_list.append(tu_row)
        print(data_list)
    return data_list


get_csv()
