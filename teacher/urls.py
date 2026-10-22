from django.contrib import admin
from django.urls import include, path
from django.shortcuts import render, redirect
from . import views

app_name = 'teacher'

def root(request):
    if request.user.is_authenticated: return redirect('teacher:dashboard')
    else: return redirect('teacher:login')


urlpatterns = [
    path('admin/',                             admin.site.urls),
    path('accounts/',                          include('allauth.urls')),
    path('',                                   root,                  name='root'),
    path('login/',                             views.signin,          name='login'),
    path('signup/',                            views.signup,          name='signup'),
    path('logout/',                            views.signout,         name='logout'),
    path('dashboard/',                         views.dashboard,       name='dashboard'),
    path('students/',                          views.students,        name='students'),
    path('manage/tests',                       views.manage_tests,    name='manage_tests'),
    path('manage/marks',                       views.manage_marks,    name='manage_marks'),
    path('students/report/<int:student_id>/',  views.generate_report, name='generate_report'),
    path('students/report/all/',               views.generate_all,    name='generate_all'),
    path('students/preview/<int:student_id>/', views.preview_report,  name='preview_report'),
]