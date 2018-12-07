from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.shortcuts import render
from sign.models import Event, Guest


def index(request):  # 初始时，返回HTML 页面
    return render(request, "index.html")


# Create your views here.
# 登录动作
def login_action(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = auth.authenticate(username=username, password=password)
        if username is not None:
            auth.login(request, user)
            request.session['user'] = username  # 将session 信息记录到浏览器
            response = HttpResponseRedirect("/event_manage/")
            # response.set_cookie("user", username, 3600)  # 添加浏览器cookie
            return response
        else:
            return render(request, "index.html", {"error": "username or password is error!"})


# 发布会管理
@login_required
def event_manage(request):
    # #username = request.COOKIES.get("user", "")  # 读取浏览器cookie
    event_list = Event.objects.all()
    username = request.session.get('user', '')  # 读取浏览器中的session
    return render(request, "event_manage.html", {"user": username, "events": event_list})


# 发布会名称搜索
@login_required
def search_name(request):
    username = request.session.get('user', '')
    search_name = request.GET.get('name', '')
    event_list = Event.objects.filter(name__contains=search_name)
    return render(request, "event_manage.html", {"user": username, "events": event_list})


# 嘉宾管理
@login_required
def guest_manage(request):
    username = request.session.get('user', '')
    guest_list = Guest.objects.all()
    return render(request, "guest_manage.html", {"user": username, "guests": guest_list})


# 嘉宾名称搜索
@login_required
def search_name(request):
    username = request.session.get('user', '')
    search_name = request.GET.get('name', '')
    guest_list = Guest.objects.filter(realname__contains=search_name)
    return render(request, "guest_manage.html", {"user": username, "guests": guest_list})
