# -*- coding:utf-8 -*-
# @Time     :2019/8/13 22:23
# @author   :Dake
# Email     :604297158@qq.com
# File      :handle_mysql.py
# @Software :PyCharm
import pymysql
import random
import os

from common.handle_conf import Config
from common.handle_dir import CONFIGS_DIR

'''
# 建立连接
conn = pymysql.connect(
    host=cf.get_value("db_msg", "host"),  # 地址
    port=cf.get_int("db_msg", "port"),  # 端口
    user=cf.get_value("db_msg", "user"),  # 用户
    pwd=cf.get_value("db_msg", "pwd"),  # 密码
    database=("db_msg", "database"),  # 库名
    charset="utf8",  #
    corsorclass=pymysql.cursors.DictCursor  # 字典游标
)

# 创建游标
cursor = conn.cursor()

# 执行sql
sql = "sql语句"
cursor.execute(sql)

# 提交，不然无法保存新建或者修改的数据
conn.commit()

# 获取结果
result1 = cursor.fetchone()  # 获取剩余第一条结果
result2 = cursor.fetchall()  # 获取剩余全部结果
result3 = cursor.fetchmany(4)  # 获取剩余结果的前4行

# 移动游标,在fetch数据时按照顺序进行，可以使用cursor.scroll(num,mode)来移动游标位置，如：
cursor.scroll(1, mode='relative')  # 相对当前位置移动
cursor.scroll(2, mode='absolute')  # 相对绝对位置移动

# 关闭游标
cursor.close()
# 关闭连接
conn.close()

# 由于默认获取的数据是元祖类型，如果想要或者字典类型的数据，即通过游标设定参数 cursor=pymysql.cursors.DictCursor
# 创建游标，游标设为字典类型
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
'''


cf = Config(os.path.join(CONFIGS_DIR, "config.conf"))


class MySql:
    """
    mysql数据库操作类
    """

    def __init__(self, user, pwd, database):
        # 建立连接
        self.conn = pymysql.connect(host=cf.get_value("db_msg", "host"),
                                    user=user,
                                    password=pwd,
                                    port=cf.get_int("db_msg", "port"),
                                    database=database,
                                    charset="utf8",
                                    cursorclass=pymysql.cursors.DictCursor)
        # 创建游标
        self.cursor = self.conn.cursor()

    def run(self, sql, args=None, is_more=False):
        """
        sql执行
        :param sql: 需要传入的sql语句
        :param args: sql语句中需要传入的条件参数,以元组的形式传入
        :return: 返回sql语句执行完成返回的结果（以字典的形式返回）
        """
        self.cursor.execute(sql, args)
        self.conn.commit()
        if is_more:
            return self.cursor.fetchall()  # 获取多条结果
        else:
            return self.cursor.fetchone()  # 获取一条结果

    def get_lastid(self, sql, args=None):
        """
        可以获取到最新自增的ID，也就是最后插入的一条数据ID
        :param sql: 需要传入的sql语句
        :param args: sql语句中需要传入的条件参数,以元组的形式传入
        :return: 返回最后插入的一条数据id
        """
        self.cursor.execute(sql, args)
        self.conn.commit()
        return self.cursor.lastrowid

    def close(self):
        self.cursor.close()
        self.conn.close()

    @staticmethod
    def create_mobile():
        """
        生成手机号码
        :return: 返回手机号码
        """
        star_mobile = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139"]
        mobile_num = random.choice(star_mobile) + "".join(random.sample("1234567890", 8))
        return mobile_num

    def is_exit_mobile(self):
        """
        判断mobile_num是否存在数据库中
        :return:
        """
        sql = "select * from member where MobilePhone = %s"
        if self.run(sql, (MySql.create_mobile(),)):  # 判断执行sql后的结果是否为空，不为空T，为空F
            return True
        else:
            return False

    def not_exit_mobile(self):
        """
        创建一个不在数据库的手机号
        :return:手机号码
        """
        while True:
            mobile_num = self.create_mobile()
            if self.is_exit_mobile():
                continue
            else:
                break
        return mobile_num

    def not_exit_memberid(self):
        """
        获取不存在的memberid
        :return:
        """
        sql = "select * from loan where MemberID = %s"
        while True:
            member_id = "".join(random.sample("1234567890", 6))
            if self.run(sql, (member_id,)):
                continue
            else:
                break
        return member_id


if __name__ == '__main__':
    mysql = MySql(cf.get_value("db_msg", "user1"), cf.get_value("db_msg", "pwd1"), cf.get_value("db_msg", "database1"))

    sql = "SELECT * FROM tag_info WHERE name='编辑73649'"

    aa = mysql.run(sql)
    print(aa)

    # result = mysql.run(sql, is_more=True)
    # print(result)
    # mysql.close()
