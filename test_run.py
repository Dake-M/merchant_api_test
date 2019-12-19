# -*- coding:utf-8 -*-
# @Time     :2019/8/13 22:28
# @author   :Dake
# Email     :604297158@qq.com
# File      :test_run.py
# @Software :
import unittest
import os
from lib.HTMLTestRunnerNew import HTMLTestRunner
from common.handle_dir import PYCASE_DIR, REPORTS_FILE_PATH, CONFIGS_DIR


# # 判断是否存在配置文件register.conf
# register_file = os.path.join(CONFIGS_DIR, "register.conf")
# if not register_file:
#     write_users_config()

suite = unittest.TestSuite()
loader = unittest.TestLoader()
discover = unittest.defaultTestLoader.discover(PYCASE_DIR, pattern="test*.py")
# suite.addTest(loader.loadTestsFromModule(test_register))
# suite.addTest(loader.loadTestsFromModule())
# suite.addTest(loader.loadTestsFromModule())
# str1 = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
description = "云缴费运营商各个模块包含的接口测试"
with open(REPORTS_FILE_PATH, "wb") as file:
    runner = HTMLTestRunner(file, verbosity=2, title="云缴费运营商接口测试报告", description=description, tester="Dake")
    runner.run(discover)