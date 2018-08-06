from django.conf.urls import url
from dk import views


urlpatterns = [
    # 通讯录数据清洗测试
    url(r'transform_user_address/',views.transform_user_address,name='transform_user_address'),
    # 通话记录数据清洗
    url(r'transform_user_log/',views.transform_user_log,name='transform_user_log'),
    # 查询频繁通话前十
    url(r'frequent_call_logs/',views.frequent_call_logs,name='frequent_call_logs'),
    # 固话查询
    url(r'fixed_line_log/',views.fixed_line_log,name='fixed_line_log'),
    # 通讯录查询
    url(r'address_list/',views.address_list,name='address_list'),
    # 获取通话记录柱状图数据
    url(r'logs_pic/',views.logs_pic,name='logs_pic'),
    # 通话记录查询分页
    url(r'applicat_logs_info/',views.applicat_logs_info,name='applicat_logs_info'),





]