from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def index(request):  # 初始时，返回HTML 页面
    return render(request, "index.html")


# Create your views here.
# 登录动作
def login_action(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        if username == "admin" and password == "123456":
            response =  HttpResponseRedirect("/event_manage/")
            #response.set_cookie("user", username, 3600)  # 添加浏览器cookie
            request.session['user'] = username  #将session 信息记录到浏览器
            return response
        else:
            return render(request, "index.html", {"error": "username or password is error!"})


# 发布会管理
def event_manage(request):
    #username = request.COOKIES.get("user", "")  # 读取浏览器cookie
    username = request.session.get('user','') #读取浏览器中的session
    return render(request, "event_manage.html", {"user": username})

