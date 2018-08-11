from django.conf.urls import url

from case import views

urlpatterns = [
   url(r'^totalcase/',views.total_case,name='total_case'),
   url(r'^unauditedcase/',views.unaudited_case,name='unaudited_case'),
   url(r'^casedetail/',views.case_detail,name='case_detail'),
   url(r'^caseaudit/',views.case_audit,name='case_audit'),
   url(r'^passcase/',views.pass_case,name='pass_case'),
   url(r'^refusecase/',views.refuse_case,name='refuse_case')
]