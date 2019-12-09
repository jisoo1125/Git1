from django.urls import path
from . import views

urlpatterns = [
    path('tailong/', views.tailong, name='tailong'),
    path('xiaoyu/',views.xiaoyu,name='xiaoyu'),
]