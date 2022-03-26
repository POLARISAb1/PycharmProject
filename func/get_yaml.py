# coding=utf-8
# 获取demo.yml文件
import pytest
import yaml


def get_yaml():
    # 读取yaml文件
    with open('../data/demo.yml', 'r') as file:
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


if __name__ == '__main__':
    get_yaml()
