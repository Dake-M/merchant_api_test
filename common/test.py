# -*- coding: utf-8 -*-
import time
import datetime
import random

# now = time.time()
# print(now)
#
#
#
# # 字符类型的时间
# now1 = datetime.datetime.now() - datetime.timedelta(days=30)
# print(now1)
# str1 = now1.strftime("%Y-%m-%d %H-%M-%S")
# print(str1)
# # 转为时间数组
# timeArray = time.localtime(now1)
# print(timeArray)
# timeArray可以调用tm_year等
# print(now1.tm_year)   # 2013
# 转为时间戳
# timeStamp = int(time.mktime(now1))
# print(timeStamp)  # 1381419600


# now = time.time()
# print("当前时间戳:%s"%now)
# #格式化年月日时分秒
# local_time = time.localtime(now)
# date_format_localtime =  time.strftime('%Y-%m-%d %H:%M:%S',local_time)
# print("格式化时间之后为:%s"%date_format_localtime)


# 字符类型的时间
# now1 = datetime.datetime.now() - datetime.timedelta(days=30)
# print(now1)
# str1 = now1.strftime("%Y-%m-%d %H:%M:%S")
# print(str1)
# # 转为时间数组
# timeArray = time.strptime(str1, "%Y-%m-%d %H:%M:%S")
# print(timeArray)
# timeStamp = int(time.mktime(timeArray))
# print(timeStamp)
list1 = []
for i in range(1, 41):
    list1.append(i)
print(list1)

a1 = random.randint(1, 40)
a2 = random.randint(1, 40)
while a1 == a2:
    a2 = random.randint(1, 40)

a3 = random.randint(1, 40)
a4 = random.randint(1, 40)
a5 = random.randint(1, 40)
a6 = random.randint(1, 40)
print(a1)

j = 0
