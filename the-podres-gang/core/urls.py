"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.contrib import admin  # mandatory import
from django.contrib.auth.decorators import login_required, login_not_required
from django.urls import path, include  # mandatory import
from features.gallery.views import Home, About, CreateImage


urlpatterns = [
    path("", login_not_required(Home.as_view()), name="home"),
    path("", include("django.contrib.auth.urls")),  # mandatory url
    path("admin/", admin.site.urls),  # mandatory url
    path("image/", include("features.gallery.urls")),
    path("about", login_not_required(About.as_view()), name="about"),
]
