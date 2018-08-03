from django.shortcuts import render
from django.http import JsonResponse


from dk.models import Users
from DK_Project import status_code


def true_info(request):
    """
    接受实名认证表单并保存进数据库
    :param request: 请求
    :return: 返回结果查看相对路径下, ../doc/api_doc/true_info.md
    """
    if request.method == 'GET':
        return render(request, 'market/uc-account.html')

    if request.method == 'POST':
        # 真实头像
        true_avatar = request.FILES.get('true_avatar')
        # 身份证号
        id_card = request.POST.get('id_card')
        # 真实名字
        true_name = request.POST.get('true_name')
        # 性别
        sex = request.POST.get('sex')
        # 电话
        tel = request.POST.get('tel')
        # 地址
        address = request.POST.get('address')
        # 详细地址
        more_address = request.POST.get('address')
        # 电子邮箱
        email = request.POST.get('email')
        # 判断是否有空的数据
        if all([true_avatar, true_name, sex, tel, address, more_address, email, id_card]):
            user = Users.objects.get(pk=1)
            try:
                # 修改当前user的实名认证信息
                user.true_name, user.true_avatar, \
                user.sex, user.tel, user.address, \
                user.more_address, user.email, user.id_card = true_name, \
                                                              true_avatar, sex, tel, address, more_address, email, id_card
                user.save()
                true_avatar_url = user.true_avatar.url
                status_code.SUCCESS['true_avatar_url'] = true_avatar_url
                return JsonResponse(status_code.SUCCESS)
            except Exception as e:
                print(e)
                return JsonResponse(status_code.USERINFO_SAVE_ERROR)
        else:
            return JsonResponse(status_code.USERINFO_TRUE_INFO_NULL)

