from django.http import Http404
from django.http import HttpResponse

# 我們要把前端template和後端views.py分開，需要load它進來
# from django.template import loader

from django.shortcuts import render

# 為了要能夠在首頁顯示出Album名稱，必須要和db連接，所以import models的class(也就是一個表)
from .models import Album


def index(request):
    # 這行會回傳一個list
    all_albums = Album.objects.all()

    # 不用寫 templates/music/index.html的原因是在做leader.get_template的時候，django已經自動去找template資料夾了
    # template = loader.get_template('music/index.html') # django.shortcuts 讓我們省略了這一行

    # 用來傳後端資料給template的一個字典 (大家都叫context，但也可以叫別的名字)
    context = {
        'all_albums': all_albums,
    }
    # 記得無論如何都要回傳request
    # return HttpResponse(template.render(context, request)) # django.shortcuts 讓我們省略了這一行

    # render其實已經幫我們回傳了一個http response
    # django.shortcuts 只要以下一行！！
    return render(request, 'music/index.html', context)


def detail(request, album_id):
    return HttpResponse("<h2>Details for album ID: " + str(album_id) + "</h2>")
