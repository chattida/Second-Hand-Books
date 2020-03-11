"""Second_hand_Books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include

from textbook import views as textbook

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('textbook.urls')),
    path('login/', textbook.login_page, name='login'),
    path('logout/', textbook.logout_page, name='logout'),
    path('register/', textbook.register_page, name='register'),
    path('post/', include('post.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
