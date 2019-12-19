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
file = Excel(CASE_FILE_PATH, "school_management")  # excel文件
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
        log.info("{:*^40s}".format("学校管理开始执行用例"))

    @classmethod
    def tearDownClass(cls):
        req.close()
        mysql.close()
        log.info("{:*^40s}".format("学校管理结束用例执行"))

    @data(*data_list)
    def test_case(self, data_dict):

        # 拼接完整的url
        new_url = cf.get_value("cases_msg", "host") + data_dict["url"]

        # 将excel中拿到的请求参数转换为字典类型
        case_data = data_dict["data"]
        if case_data:
            new_data = json.loads(Context.school_management_parametrization(case_data))
            # log.info(new_data)
        else:
            new_data = {}

        #  将excel中拿到的sql参数化
        check_sql = data_dict["check_sql"]
        if check_sql:
            new_check_sql = Context.school_management_parametrization(check_sql)

        # 将excel中拿到的headers参数化
        headers = data_dict["headers"]
        if headers:
            new_headers = json.loads(Context.school_management_parametrization(data_dict["headers"]))
            # log.info(new_headers)
        else:
            new_headers = {}

        try:
            # 发起请求
            res = req.http_request(data_dict["method"], new_url, new_data, headers=new_headers, is_json=True)
        except Exception as e:
            raise e

        if data_dict["title"] == "正常登录":
            setattr(Context, "login_key", res.json()["data"]["loginKey"])
        elif data_dict["title"] == "添加分组":
            result1 = mysql.run(new_check_sql, new_data["name"])
            setattr(Context, "group_code_re", result1["code"])
            setattr(Context, "group_id_del", str(result1["id"]))

        try:
            self.assertIn(str(data_dict["expected"]), res.text)
            if data_dict["title"] != "添加分组":
                check_sql = data_dict["check_sql"]
                if check_sql:
                    new_check_sql = Context.school_management_parametrization(check_sql)
                    result2 = mysql.run(new_check_sql, new_data["name"])
                    # log.info(result2)
                    if str(result2.get("created")) in res.text:
                        # 校验完成后，删除掉添加对应的分组数据
                        url = "https://payexp.snsshop.net/merchantadmin/school-group/del"
                        del_data = {"id": result2["id"]}
                        # log.info(del_data)
                        # log.info(result2.get("id"))
                        # log.info(result2["id"])
                        req.http_request("get", url, del_data, headers=new_headers, is_json=True)

            file.write_data(data_dict["case_id"] + 1, 7, res.text, "Pass")
            log.info("请求成功，返回结果{0}".format(res.text))

        except Exception as e:

            log.error("请求失败，返回结果{0}".format(res.text))
            file.write_data(data_dict["case_id"] + 1, 7, res.text, "Fail")
            raise e


if __name__ == "__main__":
    unittest.main()