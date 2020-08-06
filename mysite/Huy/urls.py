from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('',views.indexview, name='Home'),
    path('login/',LoginView.as_view(), name='login_url'),
    path('register/', views.registervieww, name='register'),
    path('logout/',LogoutView.as_view(next_page='login_url'), name='logout'),
    path('form/', views.formview, name='formview'),
    path('thanks/', views.thanksview, name='thanks'),
]