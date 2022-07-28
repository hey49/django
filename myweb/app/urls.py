from django.urls import path, re_path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('model/', views.model_create, name='create'),
    re_path(r'model/edit/(?P<uid>\d+)', views.model_edit, name='edit'),
    re_path(r'model/delete/(?P<uid>\d+)', views.model_delete, name='delete'),
]