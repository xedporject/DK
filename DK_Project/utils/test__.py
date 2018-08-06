import calendar
import datetime

import requests
import re
from threading import Thread


def get_adress(phone):
    query_url = '''
    https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query={}&co=&resource_id=6004&t=1533111873930&ie=utf8&oe=gbk&cb=op_aladdin_callback&format=json&tn=baidu&cb=jQuery110201329388576728905_1533102447461&_=1533102447476
    '''
    try:
        res = requests.get(query_url.format(phone))
        data = res.text
        data2 = re.findall('"city":"(.{2,4})",', data)
        data3 = re.findall('"prov":"(.{2,4})",', data)

        return '{} {}'.format(data3[0], data2[0])
    except:
        return '固话'


class MyThread(Thread):

    def __init__(self, PhoneNumber):
        Thread.__init__(self)
        self.PhoneNumber = PhoneNumber

    def run(self):
        self.result = get_adress(self.PhoneNumber)

    def get_result(self):
        return self.result


def get_month(first_day, ):
    '''
    传入某一个月的第一天的日期格式,返回上一个月的第一天日期
    :param first_day: 某一个月的第一天
    :return:
    '''
    # time = datetime.datetime.now()
    # # 当前月份的第一天
    # first_day = datetime.date(time.year, time.month, 1)
    # 获取某一个月有多少天
    days_num = calendar.monthrange(first_day.year, first_day.month)[1]

    first_day_last_one_month = first_day - datetime.timedelta(days = days_num)
    return first_day_last_one_month












