import datetime
import random
import re
import time

from xml.dom.minidom import parse
import xml.dom.minidom

from dk.models import ApplicatAddressList, ApplicationTelLog, InternetTagList
from utils.test__ import get_adress, MyThread


def transform_address(user, path):
    '''
    :param path: 用户通讯录文件地址
    :return: None
    '''
    # path = 'address_list.xml'
    if not re.findall('xml',path):
        return '文件类型错误'
    try:
        DOMTree = xml.dom.minidom.parse(r'/workspaces/DK_Project/utils/media/address_list.xml')
        collection = DOMTree.documentElement
        users_address = collection.getElementsByTagName("Contact")
    except:
        return '路径错误'
    # 互联网标签号码
    tag = {'18123464239': '邮政', '18788224590': '周姐'}
    result = InternetTagList.objects.all()
    for one in result:
        tag[one.tel] = one.tag

    for user_address in users_address:
        try:
            # 通讯录tag
            phone_name = user_address.getElementsByTagName("Name")[0].childNodes[0].data
            PhoneNumber = user_address.getElementsByTagName("Phone")[0].childNodes[0].data
            # 写入数据库
            applicataddress = ApplicatAddressList()
            applicataddress.uid = user
            applicataddress.address_name = phone_name
            applicataddress.tel = PhoneNumber
            applicataddress.inter_tag = tag[PhoneNumber] if PhoneNumber in tag.keys() else ' '

            applicataddress.save()
            # ApplicatAddressList.objects.create(uid=user.user_id, address_name=phone_name, tel=PhoneNumber)
        except:
            return '数据地址错误或数据类型错误'
        # 写入数据库
    return None


def transform_data(user,path):
    '''
    :param request: django的request参数
    :param path: 用户通话记录path
    :return: None
    '''
    if not re.findall('xml',path):
        return '文件类型错误'
    DOMTree = xml.dom.minidom.parse(r'/workspaces/DK_Project/utils/media/haisimao_log.xml')
    collection = DOMTree.documentElement

    # 在集合中获取所有通话记录
    users_name = collection.getElementsByTagName("CallLog")

    # 互联网标签号码
    tag = {'18123464239': '邮政','18788224590': '周姐'}
    result = InternetTagList.objects.all()
    for one in result:
        tag[one.tel] = one.tag

    # 数据清洗
    ths = []
    user_log = []
    for user_name in users_name:
        # 有的通话记录没有名称
        # 拿到通话数据
        try:
            # 通讯录tag
            # 主叫被叫/未接通  Flags: 1,被叫/2,主叫/3,未接
            Flags = user_name.getElementsByTagName("Flags")[0].childNodes[0].data
            # 通话时长
            Duration = user_name.getElementsByTagName("Duration")[0].childNodes[0].data
            # 通话时间
            StartTime = user_name.getElementsByTagName("StartTime")[0].childNodes[0].data
            StartTime = datetime.datetime.strptime(StartTime, '%Y-%m-%d %H:%M:%S')
            log_tag = user_name.getElementsByTagName("ContactName")[0].childNodes[0].data
            PhoneNumber = user_name.getElementsByTagName("PhoneNumber")[0].childNodes[0].data
            # 互联网标记
            inter_tag = tag[PhoneNumber] if PhoneNumber in tag.keys() else ' '
        except:
            # 通讯录tag
            log_tag = '未命名用户'
            phone_adrress = '固话'
        user_log.append([Flags, log_tag, Duration, StartTime, PhoneNumber, inter_tag])
        ths.append(MyThread(PhoneNumber))

    for i in ths:
        i.start()
    # 是在不行加一个延时
    time.sleep(10)
    for i in range(len(ths)):
        ths[i].join()
        phone_adrress = ths[i].get_result()
        # 添加归属地
        user_log[i].append(phone_adrress)
    time.sleep(10)
    for user_ in user_log:
        # 写入数据库
        ApplicationTelLog.objects.create(uid=user,
                                        inter_tag=user_[5],
                                        address_tag=user_[1],
                                        talk_date=user_[3],
                                        talk_duration=user_[2],
                                        type=user_[0],
                                        phone=user_[4],
                                        phone_address=user_[-1],
                                        sur_te_charge=random.random()*100,
                                        )

