"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.urls import path
from controller.views import *
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from dj_rest_auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordResetConfirmView,
    PasswordResetView,
    UserDetailsView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="Longanisa online",
        default_version="v1",
        description="Endpoint endpoints",
        contact=openapi.Contact(email="emmanuel.pagayonan@erpconsultancy.dev"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("flavors/", ListFlavors.as_view()),
    path("flavors/<int:pk>", RetrieveFlavor.as_view()),
    path("flavors/<int:pk>/update", UpdateFlavor.as_view()),
    path("flavors/<int:pk>/delete", DeleteFlavor.as_view()),
    path("status", AppStatus.as_view()),
    path(
        "swagger",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]

rest_urls = [
    path("auth/login/", LoginView.as_view()),
    path("auth/logout/", LogoutView.as_view()),
    path("auth/token/refresh/", TokenRefreshView.as_view()),
    path("auth/token/", TokenObtainPairView.as_view()),
    path("auth/password-change/", PasswordChangeView.as_view()),
]

urlpatterns += rest_urls