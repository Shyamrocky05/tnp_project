from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about',views.about, name='about'),
    path('training',views.training, name='training'),
    path('placements',views.placements, name='placements'),
    path('contact',views.contact, name='contact'),
    path('login',views.login, name='login'),
    path('register',views.register, name='register'),
    path('logout',views.logout, name='logout')
]
