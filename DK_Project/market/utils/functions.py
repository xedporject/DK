
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
