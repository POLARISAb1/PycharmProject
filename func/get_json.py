# coding=utf-8
# 读取json文件内容
import json


def get_json():
    """
    [[1, 1, 2], [3, 6, 9], [100, 200, 300]]
    :return:
    """
    with open('../data/params.json', 'r') as file:
        # read():一次读取文件所有内容，返回一个str
        f = file.read()
        # json.loads()：将json实例转化为python对象，返回一个字典
        data = json.loads(f)
        # 获取字典的值，返回新视图对象
        data_values = data.values()
        # 将视图对象转成列表
        print(list(data_values))
    return list(data_values)


if __name__ == '__main__':
    get_json()
