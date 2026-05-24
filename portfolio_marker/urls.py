from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.logins, name='login'),
    path('login/', views.logins, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logouts, name='logout'),
    path('select_subjects/', views.select_subjects, name='select_subjects'),
    path('business/', views.business, name='business'),
    path('business/', views.business, name='business'),
    path('business/insert/', views.business_insert, name='business_insert'),
    path('business/insert-all/', views.business_insert_all, name='business_insert_all'),
    path('business/delete/', views.business_delete, name='business_delete'),
]
