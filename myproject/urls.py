"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
from news import views  # 从应用news中导入views模块（无需../，Django会自动识别项目路径）
from debug_toolbar.toolbar import debug_toolbar_urls
urlpatterns = [
    path("admin/", admin.site.urls),
    path("articles/<int:year>/", views.year_archive),
    path("polls/", include("polls.urls")),
] + debug_toolbar_urls()


