from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.shortcuts import redirect

from books.views import my_books
from books.views import register
from books import views


urlpatterns = [
    path('', lambda req: redirect('login/')),
    path('admin/', admin.site.urls),
    path('my-books/', my_books, name='my_books'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='../templates/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/profile/', views.profile_view, name='profile'),
]
