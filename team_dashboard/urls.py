
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('dashboard.urls')),   # main app
    # path('accounts/', include('django.contrib.auth.urls')),
]
