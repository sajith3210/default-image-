from django.urls import path
from onlineshopapp import views
urlpatterns = [
    path('',views.registeraction,name='register'),
    path('login',views.login,name='login'),
    path('home',views.home,name='home'),
    path('logout',views.logout,name='logout')
]