from django.contrib import admin
from django.urls import include, path
from django.shortcuts import render, redirect
from . import views

def root(request):
    if request.user.is_authenticated: return redirect('dashboard')
    else: return redirect('login')

urlpatterns = [
    path('admin/',            admin.site.urls),
    path('accounts/',         include('allauth.urls')),
    path('',                  root,                  name='root'),
    path('login/',            views.logins,          name='login'),
    path('signup/',           views.signup,          name='signup'),
    path('logout/',           views.logouts,         name='logout'),
    path('dashboard/',        views.dashboard,       name='dashboard'),
    path('students/create/',  views.create_student,  name='create_student'),
    path('students/',         views.student,         name='student'),
    path('tests/create/',     views.create_test,     name='create_test'),
    path('tests/insert/',     views.test_insert,     name='test_insert'),
    path('tests/insert-all/', views.test_insert_all, name='test_insert_all'),
]