from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('', views.detail, name = 'detail'),
    #if non path specified forward to index
]
