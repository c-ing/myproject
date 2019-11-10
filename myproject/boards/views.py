from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# 视图是接收 httprequest 对象并返回⼀个 httpresponse 对象的Python函数
def home(request):
    boards = ["33","ww"]#Board.objects.all()
    return render(request, 'base.html', {'boards': boards})
    #return HttpResponse('Hello World!')
