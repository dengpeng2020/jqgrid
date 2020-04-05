
from django.contrib import admin
from django.urls import path, include

from stu_app import views

app_name='stu_app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("stu_list/", views.stu_list,name='stu_list'),
    path("get_stu/", views.get_stu,name='get_stu'),
    path("get_class/", views.get_class,name='get_class'),
    path("edit_stu/", views.edit_stu,name='edit_stu'),
]
