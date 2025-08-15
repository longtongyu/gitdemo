from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(requests):
    return HttpResponse("这是测试返回的数据")


def detail(requests,ids):
    return HttpResponse("这是测试返回的项目1数据",status=100)