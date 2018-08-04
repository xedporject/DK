from django.shortcuts import render


def index(request):
    """前端首页"""
    if request.method == 'GET':
        return render(request, 'home/index.html')