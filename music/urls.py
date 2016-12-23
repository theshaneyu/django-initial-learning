from django.conf.urls import url
from . import views

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),
    # /music/71
    # views.detail()不需要參數是因為前面的re已經設定是要傳的參數了(名字叫album_id)
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
]