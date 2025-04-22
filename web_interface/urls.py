"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web_interface import views
from .views import image_request  


app_name = 'web_interface'

urlpatterns = [
    path('', views.index, name='index'),

    # Image handling views
    path('live-image/', views.live_image, name='live_image'),
    path('capture/', views.capture_image, name='capture_image'),
    path('retake/', views.retake_image, name='retake_image'),
    path('image_request/', views.image_request, name='image_request'),

    # Face authentication
    path('authenticate/', views.authenticate_user, name='authenticate_user'),
]
