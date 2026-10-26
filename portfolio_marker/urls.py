from django.contrib import admin
from django.urls import path, include, re_path
from django.shortcuts import redirect

def root(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='Teachers').exists():
            return redirect('teacher:dashboard')
        else:
            return redirect('student:dashboard')

urlpatterns = [
    #path(''     ,    root),
    path('admin/',   admin.site.urls),
    path('student/', include('student.urls')),
    path('teacher/', include('teacher.urls')),
]