# -*- coding: utf-8 -*-
import requests


class Request:
    """
    接口请求类的封装
    """
    def __init__(self):
        self.session = requests.Session()   # 创建会话

    def http_request(self, method, url, data, headers, is_json=False):
        """
        请求方法的封装
        :param method:  请求类型（get，post）
        :param url: 接口请求地址
        :param data:    接口请求需要的参数
        :param headers:     接口请求需要带的表头信息
        :param is_json:     传参格式默认为非json格式
        :return:
        """

        if method.upper() == "GET":
            '''
            判断请求方式是否为get请求
            '''
            res = self.session.get(url, params=data, headers=headers, timeout=5)

        elif method.upper() == "POST":
            '''
            判断请求方式是否为post请求
            '''
            if is_json:
                res = self.session.post(url, json=data, headers=headers, timeout=5)
            else:
                res = self.session.post(url, data=data, headers=headers, timeout=5)

        else:
            res = "{0}请求方法无效".format(method)
        return res

    def close(self):
        self.session.close()


if __name__ == "__main__":
    http = Request()
    # data1 = {"username":"13222222222","password":"13222222222"}
    data = {}
    url1 = "https://payexp.snsshop.net/merchantadmin/merchant/index-dynamic-data"
    headers = {'login-key': '6c7a7fff-7435-4924-9fc3-b76fac6914a4'}
    # data2 = {"page":1,"count":15}
    # print(type(data2))
    # url2 = "https://payexp.snsshop.net/merchantadmin/school-order/get-count-list"


    # res1 = http.http_request("post", url1, data1, headers, is_json=True)
    res2 = http.http_request("post", url1, data, headers, is_json=True)

    # print(res1.json())
    print(res2.text)