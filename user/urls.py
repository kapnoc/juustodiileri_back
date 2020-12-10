from django.urls import path

from . import controlers

urlpatterns = [
    # path('', views.index, name='index'),
    path('register/', controlers.register, name='register'),
    path('login/', controlers.login_controler, name='login'),
    path('avatar/', controlers.avatar, name='avatar'),
    path('test/', controlers.test, name='test'),
    path('profile/', controlers.profile, name='profile'),
]
