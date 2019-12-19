# -*- coding:utf-8 -*-
# @Time     :2019/8/13 22:25
# @author   :Dake
# Email     :604297158@qq.com
# File      :handle_context.py
# @Software :PyCharm
import re
import os
import random
import time, datetime
from common.handle_mysql import MySql
from common.handle_conf import Config
from common.handle_dir import CONFIGS_DIR

cf = Config(os.path.join(CONFIGS_DIR, "config.conf"))


class Context:
    """
    上下文管理,参数化类
    """
    common = '\$\{(.*?)\}'  # 通用的正则匹配
    login_key1 = '\${login-key}'  # login_key
    tag_name = '\${tag_name}'  # tag_name
    tag_id = '\${tag_id}'     # tag_id
    update_tag_name = '\${update_tag_name}'  # update_tag_name
    import_student_data = '\${import_student_data}'  # 导入的学生信息
    student_id = '\${student_id}'   # 导入学生信息的学生id
    group_name_edit = '\${group_name_edit}'   # 编辑分组名
    group_name = '\${group_name}'  # 分组名
    group_code = '\${group_code}'  # 分组编码
    random_num = '\${random_num}'  # 随机数字
    re_group_code = '\${re_group_code}'  # 重复的code
    del_group_id = '\${del_group_id}'  # 删除的分组id
    star_time = '\${star_time}'  # 开始时间
    end_time = '\${end_time}'  # 结束时间
    edit_item_name = '\${edit_item_name}'  # 科目编辑名称
    item_name = '\${item_name}'     # 科目名称
    item_id = '\${item_id}'   # 科目id
    department_name = '\${department_name}'  # 部门名称
    edit_department_name = '\${edit_department_name}'  # 部门编辑名称
    department_id = '\${department_id}'  # 部门id
    position_name = '\${position_name}'  # 职位名称
    edit_position_name = '\${edit_position_name}'  # 职位编辑
    position_id = '\${position_id}'  # 职位id
    member_name = '\${member_name}'  # 成员名称
    member_phone = '\${member_phone}'  # 成员帐号
    edit_member_name = '\${edit_member_name}'  # 成员名称编辑
    member_id = '\${member_id}'  # 成员id


    @classmethod
    def login_key_replace(cls, data):
        """
        替换data中包含 ${login-key} 的参数
        :return:
        """
        while re.search(cls.login_key1, data):
            login_key = getattr(Context, "login_key")
            data = re.sub(cls.login_key1, login_key, data)
        return data

    @classmethod
    def home_page_parametrization(cls, data):
        """
        运营商首页接口数据参数化
        :return:
        """
        data = cls.login_key_replace(data)
        return data

    @classmethod
    def tag_id_replace(cls, data):
        """
        将制定的tag_id 替换给变量${tag_id}
        :param data:
        :return:
        """

        while re.search(cls.tag_id, data):
            tagid = getattr(Context, "tagid")
            data = re.sub(cls.tag_id, tagid, data)
        return data

    @classmethod
    def student_list_parametrization(cls, data):
        """
        学生列表接口数据参数化
        :param data:
        :return:
        """
        data = cls.login_key_replace(data)
        return data

    @classmethod
    def tag_name_replace(cls, data):
        """
        将随机生成的tag_name替换给变量${tag_name}
        :param data:
        :return:
        """

        while re.search(cls.tag_name, data):
            random_tag_name = "tag" + "".join(random.sample("1234567890", 5))
            data = re.sub(cls.tag_name, random_tag_name, data)
        return data

    @classmethod
    def update_tag_name_replace(cls, data):
        """
        将随机生成的update_tag_name替换给变量${update_tag_name}
        :param data:
        :return:
        """
        while re.search(cls.update_tag_name, data):
            random_update_tag_name = "编辑" + "".join(random.sample("1234567890", 5))
            data = re.sub(cls.update_tag_name, random_update_tag_name, data)
        return data

    @classmethod
    def import_student_to_tag_data(cls, data):
        """
        将配置文件的import_student_data数据替换给变量${import_student_data}
        :param data:
        :return:
        """
        while re.search(cls.import_student_data, data):
            data = re.sub(cls.import_student_data, cf.get_value("student_to_tag", "student_data"), data)
        return data

    @classmethod
    def student_id_replace(cls, data):
        """
        替换已导入学生标签下的学生id
        将配置文件的student_id数据替换给变量${student_id}
        :param data:
        :return:
        """
        while re.search(cls.student_id, data):
            import_student_id = getattr(Context, "import_student_id")
            data = re.sub(cls.student_id, str(import_student_id), data)
        return data

    @classmethod
    def tag_list_parametrization(cls, data):
        """
        标签列表接口数据参数化
        :param data:
        :return:
        """
        data = cls.login_key_replace(data)
        data = cls.tag_id_replace(data)
        data = cls.tag_name_replace(data)
        data = cls.update_tag_name_replace(data)
        data = cls.import_student_to_tag_data(data)
        data = cls.student_id_replace(data)
        return data

    @classmethod
    # group_name_edit
    def group_name_edit_replace(cls, data):
        """
        替换data中包含${group_name_edit}部分
        :param data:
        :return:
        """
        while re.search(cls.group_name_edit, data):
            random_name = "编辑" + "".join(random.sample("1234567890", 5))
            data = re.sub(cls.group_name_edit, random_name, data)
        return data

    @classmethod
    # group_name
    def group_name_replace(cls, data):
        """
        替换data中包含${group_name}部分
        :param data:
        :return:
        """
        while re.search(cls.group_name, data):
            random_name = "分组名" + "".join(random.sample("1234567890", 5))
            data = re.sub(cls.group_name, random_name, data)
        return data

    @classmethod
    # group_code
    def group_code_replace(cls, data):
        """
        替换data中包含${group_code}部分
        :param data:
        :return:
        """
        while re.search(cls.group_code, data):
            random_code = "分组编码" + "".join(random.sample("1234567890", 5))
            data = re.sub(cls.group_code, random_code, data)
        return data

    @classmethod
    # random_num
    def random_num_replace(cls, data):
        """
        替换data中包含${random_num}部分
        :param data:
        :return:
        """
        while re.search(cls.random_num, data):
            random_num = random.randint(1, 99999)
            data = re.sub(cls.random_num, str(random_num), data)
        return data

    @classmethod
    # re_group_code
    def re_group_code_replace(cls, data):
        """
        替换data中包含${re_group_code}部分
        :param data:
        :return:
        """
        while re.search(cls.re_group_code, data):
            group_code_re = getattr(Context, "group_code_re")
            data = re.sub(cls.re_group_code, group_code_re, data)
        return data

    @classmethod
    # del_group_id
    def del_group_id_replace(cls, data):
        """
        替换data中包含${del_group_id}部分
        :param data:
        :return:
        """
        while re.search(cls.del_group_id, data):
            group_id_del = getattr(Context, "group_id_del")
            data = re.sub(cls.del_group_id, group_id_del, data)
        return data

    @classmethod
    def school_management_parametrization(cls, data):
        """
        学校管理参数化
        :param data:
        :return:
        """
        data = cls.login_key_replace(data)
        data = cls.group_name_edit_replace(data)
        data = cls.group_name_replace(data)
        data = cls.group_code_replace(data)
        data = cls.random_num_replace(data)
        data = cls.re_group_code_replace(data)
        data = cls.del_group_id_replace(data)
        return data

    @staticmethod
    def get_star_time():
        """
        获取30天前的时间戳
        :return:
        """
        now1 = datetime.datetime.now() - datetime.timedelta(days=30)
        str1 = now1.strftime("%Y-%m-%d %H:%M:%S")
        time_array = time.strptime(str1, "%Y-%m-%d %H:%M:%S")
        time_stamp = int(time.mktime(time_array))
        return time_stamp

    @staticmethod
    def get_end_time():
        """
        获取结束时间的时间戳
        :return:
        """
        now1 = datetime.datetime.now()
        str1 = now1.strftime("%Y-%m-%d %H:%M:%S")
        time_array = time.strptime(str1, "%Y-%m-%d %H:%M:%S")
        time_stamp = int(time.mktime(time_array))
        return time_stamp

    @classmethod
    # star_time
    def star_time_replace(cls, data):
        """
        替换data中包含${star_time}的内容
        :param data:
        :return:
        """
        while re.search(cls.star_time, data):
            star_seaech_time = cls.get_star_time()
            data = re.sub(cls.star_time, str(star_seaech_time), data)
        return data

    @classmethod
    # end_time
    def end_time_replace(cls, data):
        """
        替换data中包含${end_time}的内容
        :param data:
        :return:
        """
        while re.search(cls.end_time, data):
            end_seaech_time = cls.get_end_time()
            data = re.sub(cls.end_time, str(end_seaech_time), data)
        return data

    @classmethod
    def report_cente_parametrization(cls, data):
        """
        学校统计表参数化
        :param data:
        :return:
        """
        data = cls.login_key_replace(data)
        data = cls.star_time_replace(data)
        data = cls.end_time_replace(data)

        return data

    @classmethod
    def edit_item_name_replace(cls, data):
        """
        edit_item_name = '\${edit_item_name}'  # 科目编辑名称
        替换data中包含${edit_item_name}的内容
        :param data:
        :return:
        """
        while re.search(cls.edit_item_name, data):
            random_name = "科目名称编辑" + "".join(random.sample("1234567890", 4))
            data = re.sub(cls.edit_item_name, random_name, data)
        return data

    @classmethod
    def item_name_replace(cls, data):
        """
        item_name = '\${item_name}'     # 科目名称
        替换data中包含${item_name}的内容
        :param data:
        :return:
        """
        while re.search(cls.item_name, data):
            random_name = "科目名称" + "".join(random.sample("1234567890", 5))
            data = re.sub(cls.item_name, random_name, data)
        return data

    @classmethod
    def item_id_replace(cls, data):
        """
        item_id = '\${item_id}'   # 科目id
        替换data中包含${item_id}的内容
        :param data:
        :return:
        """
        while re.search(cls.item_id, data):
            itemId = getattr(Context, "itemId")
            data = re.sub(cls.item_id, str(itemId), data)
        return data

    @classmethod
    def setting_center_parametrization(cls, data):
        """
        设置参数化
        :param data:
        :return:
        """
        data = cls.login_key_replace(data)
        data = cls.edit_item_name_replace(data)
        data = cls.item_name_replace(data)
        data = cls.item_id_replace(data)
        return data

    @classmethod
    def department_name_replace(cls, data):
        """
        department_name = '\${department_name}'     # 部门名称
        替换data中包含${department_name}的内容
        :param data:
        :return:
        """
        while re.search(cls.department_name, data):
            random_name = "部门名称" + "".join(random.sample("1234567890", 5))
            data = re.sub(cls.department_name, random_name, data)
        return data

    @classmethod
    def edit_department_name_replace(cls, data):
        """
        edit_department_name = '\${edit_department_name}'     # 部门编辑
        替换data中包含${edit_department_name}的内容
        :param data:
        :return:
        """
        while re.search(cls.edit_department_name, data):
            random_name = "部门编辑" + "".join(random.sample("1234567890", 5))
            data = re.sub(cls.edit_department_name, random_name, data)
        return data

    @classmethod
    def department_id_replace(cls, data):
        """
        department_id = '\${department_id}'     # 部门id
        替换data中包含${department_id}的内容
        :param data:
        :return:
        """
        while re.search(cls.department_id, data):
            del_department_id = getattr(Context, "del_department_id")
            data = re.sub(cls.department_id, str(del_department_id), data)
        return data

    @classmethod
    def position_name_replace(cls, data):
        """
        position_name = '\${position_name}'     # 职位名称
        替换data中包含${position_name}的内容
        :param data:
        :return:
        """
        while re.search(cls.position_name, data):
            random_name = "职位名称" + "".join(random.sample("1234567890", 5))
            data = re.sub(cls.position_name, random_name, data)
        return data

    @classmethod
    def edit_position_name_replace(cls, data):
        """
        edit_position_name = '\${edit_position_name}'     # 职位编辑
        替换data中包含${edit_position_name}的内容
        :param data:
        :return:
        """
        while re.search(cls.edit_position_name, data):
            random_name = "职位编辑" + "".join(random.sample("1234567890", 5))
            data = re.sub(cls.edit_position_name, random_name, data)
        return data

    @classmethod
    def position_id_replace(cls, data):
        """
        position_id = '\${position_id}'     # 职位id
        替换data中包含${position_id}的内容
        :param data:
        :return:
        """
        while re.search(cls.position_id, data):
            del_position_id = getattr(Context, "del_position_id")
            data = re.sub(cls.position_id, str(del_position_id), data)
        return data

    @classmethod
    def member_name_replace(cls, data):
        """
        member_name = '\${member_name}'  # 成员名称
        替换data中包含${member_name}的内容
        :param data:
        :return:
        """
        while re.search(cls.member_name, data):
            random_name = "成员名称" + "".join(random.sample("1234567890", 5))
            data = re.sub(cls.member_name, random_name, data)
        return data

    @classmethod
    def member_phone_replace(cls, data):
        """
        member_phone = '\${member_phone}'  # 成员帐号
        替换data中包含${member_phone}的内容
        :param data:
        :return:
        """
        star_mobile = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139"]
        while re.search(cls.member_phone, data):
            mobile_num = random.choice(star_mobile) + "".join(random.sample("1234567890", 8))
            data = re.sub(cls.member_phone, mobile_num, data)
        return data

    @classmethod
    def edit_member_name_replace(cls, data):
        """
        edit_member_name = '\${edit_member_name}'  # 成员名称编辑
        替换data中包含${edit_member_name}的内容
        :param data:
        :return:
        """
        while re.search(cls.edit_member_name, data):
            random_name = "成员编辑" + "".join(random.sample("1234567890", 5))
            data = re.sub(cls.edit_member_name, random_name, data)
        return data

    @classmethod
    def member_id_replace(cls, data):
        """
        member_id = '\${member_id}'     # 成员id
        替换data中包含${member_id}的内容
        :param data:
        :return:
        """
        while re.search(cls.member_id, data):
            del_member_id = getattr(Context, "del_member_id")
            data = re.sub(cls.member_id, str(del_member_id), data)
        return data

    @classmethod
    def manager_authority_parametrization(cls, data):
        """
        设置参数化
        :param data:
        :return:
        """
        data = cls.login_key_replace(data)
        data = cls.department_name_replace(data)
        data = cls.edit_department_name_replace(data)
        data = cls.department_id_replace(data)
        data = cls.position_name_replace(data)
        data = cls.edit_position_name_replace(data)
        data = cls.position_id_replace(data)
        data = cls.member_name_replace(data)
        data = cls.edit_member_name_replace(data)
        data = cls.member_id_replace(data)
        data = cls.member_phone_replace(data)
        return data


if __name__ == '__main__':
    one_data = '{"name":"${member_name}","mobile":"${member_phone}","password":"123456","repassword":"123456","merchantAdminDepartmentId":114,"merchantAdminPositionId":121,"isAdmin":1,"merchantPaymentSettingsIds":[-1],"schoolGroupIds":[7,8]}'
    aa = Context()
    aaaa = aa.manager_authority_parametrization(one_data)
    print(aaaa)

