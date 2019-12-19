# -*- coding: utf-8 -*-
import logging
import os
from common.handle_conf import Config
from common.handle_dir import LOG_FILE_PATH, CONFIGS_DIR, CONFIGS_FILE_PATH


cf = Config(CONFIGS_FILE_PATH)


class Log:
    """
    日志处理封装类
    """
    def __init__(self):
        self.my_logger = logging.getLogger(cf.get_value("log_msg", "logger_name"))
        self.my_logger.handlers.clear()  # 每次被调用后，清空已经存在handler
        # 定义日志级别
        # NOTSET（0），DEBUG（10），INFO（20），WARNING（30），ERROR（20），CRITICAL（50）
        # CRITICAL>ERROR>WARNING>INFO>DEBUG>NOTEST
        self.my_logger.setLevel(cf.get_value("log_msg", "log_level2"))  # 收集当前等级和当前等级以上的日志

        # 定义日志输出渠道
        console_hendle = logging.StreamHandler()  # 输出到控制台
        file_handle = logging.FileHandler(LOG_FILE_PATH, encoding='utf-8')  # 输出到文件中
        # 渠道收集的日志级别
        console_hendle.setLevel(cf.get_value("log_msg", "log_level4"))
        file_handle.setLevel(cf.get_value("log_msg", "log_level2"))

        # 定义日志显示的格式
        console_formatter = logging.Formatter(cf.get_value("log_msg", "console_formatter"))
        file_formatter = logging.Formatter(cf.get_value("log_msg", "file_formatter"))
        console_hendle.setFormatter(console_formatter)
        file_handle.setFormatter(file_formatter)

        # 日志收集器与输出渠道对
        self.my_logger.addHandler(console_hendle)
        self.my_logger.addHandler(file_handle)

    def get_logger(self):
        """
        获取日志对象
        :return:
        """
        return self.my_logger


if __name__ == "__main__":
    log = Log().get_logger()
    log.debug("这是一个debug日志")  # 手动记录日志
    log.info("这是一个info日志")
    log.warning("这是一个warning日志")
    log.error("这是一个error日志")
    log.critical("这是一个critical日志")