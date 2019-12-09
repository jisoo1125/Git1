from django.shortcuts import render

# Create your views here.


def tailong(request):
    return render(request, 'tailong.html')

def xiaoyu(request):
    return render(request,'xiaoyu.html')