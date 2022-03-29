# coding=utf-8
import yaml


class GetYaml:

    def __init__(self):
        self.li_e = []
        self.li_n = []
        self.list_key = []
        self.list_test_normal_key = []
        self.list_test_error_key = []

    def get_yaml(self):
        # 读取yaml文件
        with open('../data/test_data.yml', 'r', encoding="utf-8") as file:
            # 一次读取文件所有内容，返回一个`str`
            yaml_file = file.read()
        # 将读取到的str转化为字典格式
        deal_file = yaml.safe_load(yaml_file)
        # 开始拆分数据
        """
        {'test_normal': 
            {'Ca_add_001': 
                {'num1': 1, 'num2': 1, 'excepted': 2}
            }
        }
        """
        # 首先获取两种测试类型
        key = deal_file.keys()
        self.list_key = list(key)
        # print(self.list_key)
        """
        ['test_normal', 'test_error']
        """
        # 在获取测试用例的名字
        value = deal_file.values()
        list_value = list(value)
        li1 = list_value[0]
        li2 = list_value[1]
        test_normal_key = li1.keys()
        self.list_test_normal_key = list(test_normal_key)
        test_error_key = li2.keys()
        self.list_test_error_key = list(test_error_key)
        # 在获取测试用例的值
        test_normal_value = li1.values()
        list_normal_value = list(test_normal_value)
        test_error_value = li2.values()
        list_error_value = list(test_error_value)
        """
        [{'numa': '文', 'numb': 9.3, 'resulted': 'TypeError'}]
        """

        for i in range(7):
            normal_value = list_normal_value[i].values()
            list_normal = list(normal_value)
            self.li_n.append(list_normal)
        # print(self.li_n)
        for i in range(1):
            error_value = list_error_value[i].values()
            list_error = list(error_value)
            self.li_e.append(list_error)
        # print(self.li_e)
        return self.list_key, self.list_test_error_key, self.list_test_error_key, self.li_n, self.li_e


# yml = GetYaml()
# yml.get_yaml()
# print(yml.li_e)
# print(yml.li_n)
# print(yml.list_test_error_key)
# print(yml.list_test_normal_key)
# print(yml.list_key)
