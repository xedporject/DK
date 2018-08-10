

import random
from urllib import parse
import http.client
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from user.models import Users


def code(request):
    if request.method == 'GET':
        mobile = request.GET.get('user_tel')
        verification_code = ''
        for i in range(6):
            num = random.randint(0, 9)
            verification_code += str(num)
        text = "您的验证码是：" + verification_code + "。请不要把验证码泄露给其他人。"
        # 将验证码 存在COOKIEs中，比较使用
        response = HttpResponseRedirect('/loan/user_register/')
        response.set_cookie('verification_code', verification_code, expires=60)

        # 将验证码发送到手机上
        account = "C30434922"
        password = "bd99de175acab46b0817f52c20eab3f5"
        host = "106.ihuyi.com"
        sms_send_uri = "/webservice/sms.php?method=Submit"
        params = parse.urlencode(
            {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'})
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        conn = http.client.HTTPConnection(host, port=80, timeout=30)
        conn.request("POST", sms_send_uri, params, headers)
        conn.getresponse()
        conn.close()
        return response


def user_register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        mobile = request.POST.get('user_tel')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        # 页面上输入的验证码
        htmlverification_code = request.POST.get('verification_code')
        # 发送给手机的验证码
        mobileverification_code = request.COOKIES.get('verification_code')
        if Users.objects.filter(tel=mobile).exists():
            if password == repassword and mobileverification_code == htmlverification_code:
                password = make_password(password)
                Users.objects.create(
                    user_name=username,
                    password=password,
                    tel=mobile
                )
                return HttpResponseRedirect(reverse('loan:user_login'))
        return render(request, 'user/register.html', {'name': '用户名已存在'})


def user_login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')

        if Users.objects.filter(user_name=name).exists():

            user = Users.objects.get(user_name=name)
            if check_password(password, user.password):
                request.session['user_id'] = user.user_id
                return HttpResponseRedirect(reverse('loan:index'))
            else:
                return render(request, 'user/login.html', {'password': '用户密码错误'})
        else:
            return render(request, 'user/login.html', {'name': '用户不存在'})


def index(request):
    # 判断用户是否登录
    if 'user_id' in request.session:
        # 获取到登录用户id
        user_id = request.session.get('user_id')
        return render(request, 'user/index.html')
    else:
        return render(request, 'user/login.html')


def edit_password(request):
    if request.method == 'GET':
        return render(request, 'user/edit_password.html')
    if request.method == 'POST':
        mobile = request.POST.get('user_tel')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        if Users.objects.filter(tel=mobile).exists():
            user = Users.objects.get(tel=mobile)
            if password == repassword:
                password = make_password(password)
                user.password = password
                user.save()
                return HttpResponseRedirect(reverse('loan:user_login'))
            else:
                return render(request, 'user/login.html', {'password': '两次输入密码不一致'})
        else:
            return render(request, 'user/register.html', {'name': '用户不存在'})


def user_logout(request):
    del request.session['user_id']
    return HttpResponseRedirect(reverse('loan:user_login'))
