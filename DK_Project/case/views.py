from datetime import datetime

from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse

from dk.models import Caseform


def total_case(request):
    """
    总订单查询
    """
    if request.method == 'GET':
        # 分页显示总订单
        page_num = request.GET.get('page_num', 1)
        case = Caseform.objects.filter(cstatus_id__gte=3)
        paginator = Paginator(case, 3)
        pages = paginator.page(int(page_num))
        data = {
            'case': case,
            'pages': pages
        }
        return render(request, 'admin/case_totallist.html', data)


def unaudited_case(request):
    """
    审核订单
    """
    if request.method == 'GET':
        # 分页显示未审核订单
        page_num = request.GET.get('page_num', 1)
        case = Caseform.objects.filter(cstatus_id=4)
        paginator = Paginator(case, 3)
        pages = paginator.page(int(page_num))
        data = {
            'case': case,
            'pages': pages
        }
        return render(request, 'admin/case_unaudited.html', data)


def case_detail(request):
    """
    订单详情
    """
    if request.method == 'GET':
        case_id = request.GET.get('case_id')
        case = Caseform.objects.filter(case_id=case_id).first()
        return render(request, 'admin/case_detail.html', {'case':case})


def case_audit(request):
    """
    审核结果提交
    """
    if request.method == 'GET':
        case_id = request.GET.get('case_id')
        case = Caseform.objects.filter(case_id=case_id).first()
        return render(request, 'admin/case_audit.html', {'case':case})


def pass_case(request):
    """
    审核通过
    """
    if request.method == 'POST':
        examin_result = request.POST.get('examin_result')
        case_id = request.POST.get('case_id')
        case = Caseform.objects.filter(case_id=case_id).first()
        case.examin_result = examin_result
        case.cstatus_id = 5
        dtime = datetime.now()
        case.loan_time = dtime.strftime('%Y-%m-%d %H:%M:%S')
        # 审核人员
        # manager = request.manager
        # case.exa_admin_id = manager
        case.save()
        return JsonResponse({'code':200, 'msg':'请求成功'})


def refuse_case(request):
    """
    审核拒绝
    """
    if request.method == 'POST':
        examin_result = request.POST.get('examin_result')
        case_id = request.POST.get('case_id')
        case = Caseform.objects.filter(case_id=case_id).first()
        case.examin_result = examin_result
        case.cstatus_id = 6
        dtime = datetime.now()
        case.loan_time = dtime.strftime('%Y-%m-%d %H:%M:%S')
        # dtime = datetime.now()
        # case.start_time = dtime.strftime('%Y-%m-%d %H:%M:%S')
        # manager = request.manager
        # case.exa_admin_id = manager
        case.save()
        return JsonResponse({'code':200, 'msg':'请求成功'})
