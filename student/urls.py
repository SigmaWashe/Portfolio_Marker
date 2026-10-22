from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

from student import views

app_name = 'student'

def root(request):
    if request.user.is_authenticated: return redirect('student:dashboard')
    else: return redirect('student:login')

urlpatterns = [
    path('admin/',                                 admin.site.urls),
    path('accounts/',                              include('allauth.urls')),
    path('',                                       root,                     name='root'),
    path('login/',                                 views.signin,             name='login'),
    path('signup/',                                views.signup,             name='signup'),
    path('logout/',                                views.logouts,            name='logout'),
    path('complete-profile/',                      views.complete_profile,   name='complete_profile'),
    path('select-subjects/',                       views.select_subjects,    name='select_subjects'),
    path('dashboard/',                             views.dashboard,          name='dashboard'),
    path('subject/<str:subject_name>/',            views.subject,            name='subject'),
    path('subject/<str:subject_name>/insert/',     views.subject_insert,     name='subject_insert'),
    path('subject/<str:subject_name>/insert-all/', views.subject_insert_all, name='subject_insert_all'),
    path('subject/<str:subject_name>/delete/',     views.subject_delete,     name='subject_delete'),
    path('subject/<str:subject_name>/manage/',     views.manage_tests,       name='manage_tests'),
    path('subject/<str:subject_name>/report/',     views.generate_report,    name='generate_report'),
    path('subject/<slug:subject_name>/preview/',   views.preview_report,     name='preview_report'),
]