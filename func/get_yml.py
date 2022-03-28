# coding=utf-8
import yaml


def get_values():
    # 读取yaml文件
    with open('../data/test.yml', 'r', encoding="utf-8") as file:
        # 一次读取文件所有内容，返回一个`str`
        yaml_file = file.read()
        # print(type(yaml_file), yaml_file)
        # 将读取到的str转化为字典格式
        deal_file = yaml.safe_load(yaml_file)
        # print(type(deal_file), deal_file)
    # # 获取要测试的值
    result = deal_file.values()
    list_r = list(result)
    print(list_r)
    return list_r


def get_key():
    # 读取yaml文件
    with open('../data/test.yml', 'r', encoding="utf-8") as file:
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


if __name__ == '__main__':
    get_values()
    get_key()
