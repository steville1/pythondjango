

from django.conf.urls import url
from .import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.create, name='create'),
    url(r'^list/$', views.listdata, name='listdata'),
    
]