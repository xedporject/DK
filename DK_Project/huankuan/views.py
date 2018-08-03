from django.shortcuts import render


def order_detail(request):
    if request.method == 'GET':
        return render(request, 'admin/order_detail.html')