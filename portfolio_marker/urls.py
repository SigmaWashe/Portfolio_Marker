from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.logins, name='login'),
    path('login/', views.logins, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logouts, name='logout'),
    path('business/', views.business, name='business'),
]
