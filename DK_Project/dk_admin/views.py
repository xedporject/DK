from django.shortcuts import render


def admin(request):
    if request.method == 'GET':
        return render(request, 'admin/index.html')


def top(request):
    if request.method == 'GET':
        return render(request, 'admin/top.html')


def bar(request):
    if request.method == 'GET':
        return render(request, 'admin/bar.html')


def menu(request):
    if request.method == 'GET':
        return render(request, 'admin/menu.html')


def main(request):
    if request.method == 'GET':
        return render(request, 'admin/main.html')


def order_list(request):
    if request.method == 'GET':
        return render(request, 'admin/order_list.html')
