from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),  # Это должно быть основным маршрутом
    path('home', views.home, name='home'),  # Перенесли старый home в отдельный маршрут
    path('admin', admin.site.urls),
    path('premium', views.premium, name='premium'),
    path('praktikum', views.praktikum, name='praktikum'),
    path('documents', views.documents, name='documents'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
