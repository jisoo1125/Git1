from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def tailong(request):
    return render(request, 'tailong.html')


def xiaoyu(request):
    return render(request,'xiaoyu.html')


def wxun(request):
    return render(request,'wxun.html')


def zxy(request):
    return render(request,'zhaoxinyu.html')