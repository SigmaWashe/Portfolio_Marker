from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def root(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return redirect('login')

urlpatterns = [
    path('admin/',   admin.site.urls),
    path('student/', include('student.urls')),
    path('teacher/', include('teacher.urls')),
]