from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('model/', views.model_create, name='create'),
    path('model/edit/(?P<uid>\d+)', views.model_edit, name='edit'),
]