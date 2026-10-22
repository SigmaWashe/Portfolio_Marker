from django.contrib import admin
from django.urls import path, include, reverse
from django.shortcuts import redirect

urlpatterns = [
    path('admin/',   admin.site.urls),
    path('student/', include('student.urls')),
    #path('teacher/', include('teacher.urls')),
]