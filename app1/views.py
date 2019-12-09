from django.shortcuts import render

# Create your views here.


def tailong(request):
    return render(request, 'tailong.html')