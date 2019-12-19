# -*- coding:utf-8 -*-
# @Time     :2019/8/13 22:21
# @author   :Dake
# Email     :604297158@qq.com
# File      :handle_conf.py
# @Software :
from configparser import ConfigParser
from common.handle_dir import CONFIGS_FILE_PATH


class Config:
    '''
    配置文件的常用操作
    '''

    def __init__(self, file_name):
        self.file_name = file_name
        self.config = ConfigParser()
        self.config.read(self.file_name, encoding="utf-8")

    def get_value(self, section, option):  # 获取配置文件中某项值。返回的是str
        return self.config.get(section, option)

    def get_int(self, section, option):  # 获取配置文件中某项值。返回的是int
        return self.config.getint(section, option)

    def get_float(self, section, option):  # 获取配置文件中某项值。返回的是float
        return self.config.getfloat(section, option)

    def get_boolean(self, section, option):  # 获取配置文件中某项值。返回的是boolean
        return self.config.getboolean(section, option)

    def get_eval_data(self, section, option):  # 获取列表、元组、字典类型
        return eval(self.get_value(section, option))

    @staticmethod
    def write_config(datas, file_name, is_cover=True):
        """
        将数据写入配置文件,通过is_cover判断是否需要累加或是覆盖
        :param datas:
        :param file_name:
        :param is_cover:
        :return:
        """
        config = ConfigParser()
        if is_cover:
            if isinstance(datas, dict):
                for value in datas.values():
                    if not isinstance(value, dict):
                        return "数据不合法，应为嵌套字典的字典"
                    else:
                        for key in datas:
                            config[key] = datas[key]
                        with open(file_name, "w")as f:
                            config.write(f)
            else:
                return "数据不合法，应为嵌套字典的字典"
        else:
            if isinstance(datas, dict):
                for value in datas.values():
                    if not isinstance(value, dict):
                        return "数据不合法，应为嵌套字典的字典"
                    else:
                        for key in datas:
                            config[key] = datas[key]
                        with open(file_name, "a")as f:
                            config.write(f)
            else:
                return "数据不合法，应为嵌套字典的字典"

    @staticmethod
    def write_to_conf(datas, file_name):
        """
        将数据写入配置文件（在尾部写入（累加））
        :param datas:
        :param file_name:
        :return:
        """
        config = ConfigParser()
        if isinstance(datas, dict):
            for value in datas.values():
                if not isinstance(value, dict):
                    return "数据不合法，应为嵌套字典的字典"
                else:
                    for key in datas:
                        config[key] = datas[key]
                    with open(file_name, "w")as f:
                        config.write(f)
        else:
            return "数据不合法，应为嵌套字典的字典"


if __name__ == "__main__":
    cf = Config(CONFIGS_FILE_PATH)
    dd = cf.get_value("db_msg", "database1")
    print(dd)