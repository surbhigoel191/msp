from django.urls import path
from . import views
urlpatterns = [
    path('login', views.login, name='login'),
    path('', views.welcome, name='welcome'),
    path('login/instructions/test', views.test, name='test'),
    path('login/instructions', views.instructions, name='instructions'),
]