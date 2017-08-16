from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^talk$', views.talk, name='talk'),
    url(r'^ajax/send_message$', views.send_message, name='send_message')
]