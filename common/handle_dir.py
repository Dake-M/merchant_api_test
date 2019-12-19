# -*- coding:utf-8 -*-
# @Time     :2019/8/13 22:22
# @author   :Dake
# Email     :604297158@qq.com
# File      :handle_dir.py
# @Software :PyCharm
import os
from datetime import datetime

# 根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 配置文件目录
CONFIGS_DIR = os.path.join(BASE_DIR, "configs")
CONFIGS_FILE_PATH = os.path.join(CONFIGS_DIR, "config.conf")


# 用例文件目录
CASE_DIR = os.path.join(BASE_DIR, "data_excel")
CASE_FILE_PATH = os.path.join(CASE_DIR, "cases.xlsx")
PYCASE_DIR = os.path.join(BASE_DIR, "test_cases_py")


# 日志文件目录
LOGS_DIR = os.path.join(BASE_DIR, "logs")
LOG_FILE_PATH = os.path.join(LOGS_DIR, "log.log")

# 报告文件目录
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
str1 = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
report_name = "report_{0}.html".format(str1)
REPORTS_FILE_PATH = os.path.join(REPORTS_DIR, report_name)


if __name__ == '__main__':
    print(BASE_DIR)
    print(CONFIGS_DIR)
