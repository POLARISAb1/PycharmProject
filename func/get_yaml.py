# coding=utf-8
# 获取demo.yml文件
import pytest
import yaml


def get_value():
    # 读取yaml文件
    with open('../data/demo.yml', 'r', encoding="utf-8") as file:
        # 一次读取文件所有内容，返回一个`str`
        yaml_file = file.read()
        # print(type(yaml_file), yaml_file)
        # 将读取到的str转化为字典格式
        deal_file = yaml.safe_load(yaml_file)
        # print(type(deal_file), deal_file)
    # 获取要测试的值
    result = deal_file.values()
    list_r = list(result)
    # print(list_r)
    li = []
    for item in list_r:
        item_result = item.values()
        list_item = list(item_result)
        # print(list_item)
        li.append(list_item)
    print(li)
    return li


def get_keys():
    # 读取yaml文件
    with open('../data/demo.yml', 'r', encoding="utf-8") as file:
        # 一次读取文件所有内容，返回一个`str`
        yaml_file = file.read()
        # print(type(yaml_file), yaml_file)
        # 将读取到的str转化为字典格式
        deal_file = yaml.safe_load(yaml_file)
        # print(type(deal_file), deal_file)
        file_key = deal_file.keys()
        list_key = list(file_key)
        print(list_key)
    return list_key


def get_errvalue():
    # 读取yaml文件
    with open('../data//error.yml', 'r', encoding="utf-8") as f:
        # 一次读取文件所有内容，返回一个`str`
        yaml_err = f.read()
        # print(type(yaml_file), yaml_file)
        # 将读取到的str转化为字典格式
        deal_err = yaml.safe_load(yaml_err)
        # print(type(deal_file), deal_file)
    # 获取要测试的值
    result1 = deal_err.values()
    list_e = list(result1)
    # print(list_r)
    lis = []
    for item in list_e:
        item_result = item.values()
        list_item = list(item_result)
        # print(list_item)
        lis.append(list_item)
    print(lis)
    return lis


def get_ekeys():
    # 读取yaml文件
    with open('../data/error.yml', 'r', encoding="utf-8") as f1:
        # 一次读取文件所有内容，返回一个`str`
        yaml_file1 = f1.read()
        # print(type(yaml_file), yaml_file)
        # 将读取到的str转化为字典格式
        deal_file1 = yaml.safe_load(yaml_file1)
        # print(type(deal_file), deal_file)
        file_key1 = deal_file1.keys()
        list_key1 = list(file_key1)
        print(list_key1)
    return list_key1


if __name__ == '__main__':
    get_value()
    get_keys()
    get_errvalue()
    get_ekeys()

