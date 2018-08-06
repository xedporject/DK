import datetime

from django.core.paginator import Paginator
from django.db import connection
from django.db.models import Q, F
from django.http import JsonResponse
from django.shortcuts import render

from DK_Project.settings import PAGE_NUM
from dk.models import Users, ApplicationTelLog, ApplicatAddressList
from utils.data_transform import transform_address, transform_data
from utils.test__ import get_month


def transform_user_address(request):
    '''
    对用户的通讯录进行读取,保存
    :param request:
    :return:
    '''
    if request.method == 'GET':
        try:
            # 获取用户
            # user = request.user
            user = Users.objects.filter(user_id=1).first()
            # 查出用户上传的通讯录路径
            path = '/workspaces/DK_Project/utils/media/address_list.xml'
            data = transform_address(user, path)
            # print(data)
        except:
            return JsonResponse({'code': 400})
        return JsonResponse({'code': 200})


def transform_user_log(request):
    '''
    对用户的通话记录进行读取,保存
    :param request:
    :return:
    '''
    if request.method == 'GET':
        try:
            # 获取用户
            # user = request.user
            user = Users.objects.filter(user_id=1).first()
            # 查出用户上传的通话记录路径
            path = '/workspaces/DK_Project/utils/media/address_list.xml'
            data = transform_data(user, path)
            # print(data)
        except:
            return JsonResponse({'code': 400})
        return JsonResponse({'code': 200})


def frequent_call_logs(request):
    '''
    查询通话记录前十的通话记录
    :param request:
    :return: 通话前十的通话且查出前十通话phone与联系人最近一个月的通话
    '''
    if request.method == 'GET':
        select_sql = '''
                       select * from 
(select inter_tag,address_tag,talk_date,talk_duration,type,phone_address,sur_te_charge,phone,count(phone) 
from (select * from {} where uid=1) t1
group by phone 
order by count(phone) desc
limit 0 ,10) t3
left outer join
(select phone,count(phone) as last_month
from (select * from {} where uid=1 and talk_date >= '2018-07-01') t1
group by phone 
order by count(phone) desc) t2
on t2.phone=t3.phone;
                      '''
        tb_name = ApplicationTelLog.tb_name
        #   fetchone有点像iter() 里的__next__() 并且返回一个元组
        #   fetchone 的返回类型可以修改(cursorclass),默认返回包含数据的元组
        # cursorclass = MySQLdb.cursors.DictCursor
        with connection.cursor() as cursor:
            cursor.execute(select_sql.format(tb_name,tb_name), None)
            result = [list(one) for one in cursor.fetchall()]
        data = {
            'code': 200,
            'result': result,
        }
        return JsonResponse(data)
    if request.method == 'POST':
        pass


def fixed_line_log(request):
    '''
    获取固话通话记录
    :param request:
    :return: 固话记录
    '''
    if request.method == 'GET':
        fix_logs = ApplicationTelLog.objects.filter(Q(uid=1) & Q(phone_address='固话')).order
        data = {
            'code': 200,
            # 'result': [model_to_dict(one) for one in fix_logs],
            'result': [one.dict_() for one in fix_logs],
        }
        return JsonResponse(data)
    if request.method == 'POST':
        pass


def address_list(request):
    '''
    所有通讯录
    :param request:
    :return:
    '''
    if request.method == 'GET':
        address_lists = ApplicatAddressList.objects.all()
        data = {
            'code': 200,
            'result': [one.dict_() for one in address_lists],
        }
        return JsonResponse(data)
    if request.method == 'POST':
        pass


def applicat_logs_info(request):
    '''
    所有通话记录
    :param request:
    :return:
    '''
    if request.method == 'GET':
        tel_logs = ApplicationTelLog.objects.all()
        # 分页函数,参数一:要分页的对象,参数二:一页有几个记录
        # 将一个查询分为很多块(页)
        page_num = request.GET.get('page_num', 1)
        paginator = Paginator(tel_logs, PAGE_NUM)
        pages = paginator.page(int(page_num))
        return render(request, 'admin/applicat_tel_logs.html', {'pages': pages})

    if request.method == 'POST':
        pass


def logs_pic(request):
    '''
    查询通话记录,上五个月的所有通话记录
    :param request:
    :return:
    '''
    if request.method == 'GET':
        # 拿到前五个月的日期
        time = datetime.datetime.now()
        # 当前月份的第一天
        first_day = datetime.date(time.year, time.month, 1)
        # 上一个月的第一天
        one_month = get_month(first_day)
        two_month = get_month(one_month)
        three_month = get_month(two_month)
        four_month = get_month(three_month)
        five_month = get_month(four_month)
        user = Users.objects.filter(user_id=1).first()
        # 得到一个月的通话次数
        user_logs_one_month = ApplicationTelLog.objects.filter(Q(uid=user.user_id) & Q(talk_date__gt=one_month)).count()

        user_logs_two_month = ApplicationTelLog.objects.filter(Q(uid=user.user_id) & Q(talk_date__gt=two_month) & Q(talk_date__lt=one_month)).count()

        user_logs_three_month = ApplicationTelLog.objects.filter(Q(uid=user.user_id) & Q(talk_date__gt=three_month) & Q(talk_date__lt=two_month)).count()

        user_logs_four_month = ApplicationTelLog.objects.filter(Q(uid=user.user_id) & Q(talk_date__gt=four_month) & Q(talk_date__lt=three_month)).count()

        user_logs_five_month = ApplicationTelLog.objects.filter(Q(uid=user.user_id) & Q(talk_date__gt=five_month) & Q(talk_date__lt=four_month)).count()

        data = {
            'code': 200,
            'user_name': user.user_name,
            'user_logs_one_month': user_logs_one_month,
            'user_logs_two_month': user_logs_two_month,
            'user_logs_three_month': user_logs_three_month,
            'user_logs_four_month': user_logs_four_month,
            'user_logs_five_month': user_logs_five_month,
        }
        return JsonResponse(data)


#定时任务: 使用linux调度crontab -e



























