# -*- coding: utf-8 -*-
import unittest
import json
from lib.ddt import ddt, data
from common.handle_log import Log
from common.handle_request import Request
from common.handle_excel import Excel
from common.handle_dir import CASE_FILE_PATH, CONFIGS_FILE_PATH
from common.handle_conf import Config
from common.handle_context import Context
from common.handle_mysql import MySql


cf = Config(CONFIGS_FILE_PATH)  # 配置文件对象
file = Excel(CASE_FILE_PATH, "manager_authority")  # excel文件
data_list = file.get_cases()    # 获取文件中的数据
log = Log().get_logger()    # 日志对象
req = Request()  # 请求对象

# 创建mysql连接对象（连接的是payment库）
mysql = MySql(cf.get_value("db_msg", "user1"), cf.get_value("db_msg", "pwd1"), cf.get_value("db_msg", "database1"))


@ddt
class Testcase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        初始化
        :return:
        """
        log.info("{:*^40s}".format("权限管理开始执行用例"))

    @classmethod
    def tearDownClass(cls):
        mysql.close()
        req.close()
        log.info("{:*^40s}".format("权限管理结束用例执行"))

    @data(*data_list)
    def test_case(self, data_dict):

        # 拼接完整的url
        new_url = cf.get_value("cases_msg", "host") + data_dict["url"]
        new_url = Context.manager_authority_parametrization(new_url)

        # 将excel中拿到的请求参数转换为字典类型
        case_data = data_dict["data"]
        if case_data:
            new_data = json.loads(Context.manager_authority_parametrization(case_data))
            # log.info(new_data)
        else:
            new_data = {}

        # 将excel中拿到的headers参数化
        headers = data_dict["headers"]
        if headers:
            new_headers = json.loads(Context.manager_authority_parametrization(data_dict["headers"]))
            # log.info(new_headers)
        else:
            new_headers = {}

        #  将excel中拿到的sql参数化
        check_sql = data_dict["check_sql"]
        if check_sql:
            new_check_sql = Context.manager_authority_parametrization(check_sql)

        try:
            # 发起请求
            res = req.http_request(data_dict["method"], new_url, new_data, headers=new_headers, is_json=True)
        except Exception as e:
            raise e

        if data_dict["title"] == "正常登录":
            setattr(Context, "login_key", res.json()["data"]["loginKey"])
        elif data_dict["title"] == "添加部门":
            result1 = mysql.run(new_check_sql, new_data["name"])
            setattr(Context, "del_department_id", result1.get("id"))
        elif data_dict["title"] == "添加职位":
            result1 = mysql.run(new_check_sql, new_data["name"])
            setattr(Context, "del_position_id", result1.get("id"))
        elif data_dict["title"] == "添加成员（是负责人）":
            result1 = mysql.run(new_check_sql, new_data["name"])
            setattr(Context, "del_member_id", result1.get("id"))

        try:
            self.assertIn(str(data_dict["expected"]), res.text)
            file.write_data(data_dict["case_id"] + 1, 7, res.text, "Pass")
            log.info("请求成功，返回结果{0}".format(res.text))

        except Exception as e:

            log.error("请求失败，返回结果{0}".format(res.text))
            file.write_data(data_dict["case_id"] + 1, 7, res.text, "Fail")
            raise e


if __name__ == "__main__":
    unittest.main()