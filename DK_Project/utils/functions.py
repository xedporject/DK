
from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from rest_framework.renderers import JSONRenderer


def is_login(func):
    """登陆验证装饰器"""
    def wrapper(request):
        ticket = request.COOKIES.get("ticket")
        if not ticket:
            return HttpResponseRedirect(reverse("market:index"))
        User = None
        user = User.objects.filter(ticket=ticket)
        if not user:
            return HttpResponseRedirect(reverse('market:index'))
        return func(request)
    return wrapper


class CustomJsonRenderer(JSONRenderer):
    """
    用于返回自定义数据结构的类

    Restframework 每次在返回数据时会调用下面的方式来组装数据， 主要是重写Render方法
    """

    def render(self, data, accepted_media_type=None, renderer_context=None):
        # 判断 renderer_context 是否存在
        if renderer_context:
            # 判断数据类型是否是字典
            if isinstance(data, dict):
                code = data.pop('code', 0)
                msg = data.pop("msg", '请求成功')
            # 当数据类型不是字典时
            else:
                code = 0
                msg = '请求成功'
            response_dict = {
                'code': code,
                'msg': msg,
                'data': data,
            }
            return super().render(response_dict, accepted_media_type, renderer_context)
        # 当没有 renderer_context 时
        else:
            return super().render(data, accepted_media_type, renderer_context)
