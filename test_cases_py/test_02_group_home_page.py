# -*- coding:utf-8 -*-
import unittest
import json
from lib.ddt import ddt, data
from common.handle_log import Log
from common.handle_request import Request
from common.handle_excel import Excel
from common.handle_dir import CASE_FILE_PATH, CONFIGS_FILE_PATH
from common.handle_conf import Config
from common.handle_context import Context


cf = Config(CONFIGS_FILE_PATH)  # 配置文件对象
file = Excel(CASE_FILE_PATH, "home_page")  # excel文件
data_list = file.get_cases()    # 获取文件中的数据
log = Log().get_logger()    # 日志对象
req = Request()  # 请求对象

@ddt
class Testcase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        初始化
        :return:
        """
        log.info("{:*^40s}".format("运营商首页开始执行用例"))

    @classmethod
    def tearDownClass(cls):
        req.close()
        log.info("{:*^40s}".format("运营商首页结束用例执行"))

    @data(*data_list)
    def test_case(self, data_dict):

        # 拼接完整的url
        new_url = cf.get_value("cases_msg", "host") + data_dict["url"]

        # 将excel中拿到的请求参数转换为字典类型
        case_data = data_dict["data"]
        if case_data:
            new_data = json.loads(case_data)
        else:
            new_data = {}

        # 将excel中拿到的headers参数化
        headers = data_dict["headers"]
        if headers:
            new_headers = json.loads(Context.login_key_replace(data_dict["headers"]))
        else:
            new_headers = {}

        try:
            # 发起请求
            res = req.http_request(data_dict["method"], new_url, new_data, headers=new_headers, is_json=True)
        except Exception as e:
            raise e

        if data_dict["title"] == "正常登录":
            setattr(Context, "login_key", res.json()["data"]["loginKey"])

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