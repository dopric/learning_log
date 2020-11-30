""" This are urls for the learning_logs application"""

from django.conf.urls import url
from . import views

app_name ="learning_logs"

urlpatterns = [
    url(r'^$',  views.index, name="index"),
    url('about', views.about, name="about"),
    url('contact', views.contact, name="contact"),
    url(r'^topic/(?P<topic_id>\d+$)', views.topic, name="topic"),
    url(r'^entry/(?P<entry_id>\d+$)', views.entry, name="entry"),
    url(r'^topic/edit/(?P<topic_id>\d+$)', views.edit, name="edit")
]