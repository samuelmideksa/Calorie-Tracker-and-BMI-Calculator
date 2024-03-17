"""
URL configuration for ProjectCalories project.

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
from main import views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-meal/', views.add_meal, name="add_meal"),
    path('', views.read_meal, name="read_meal"),
    path('delete-meal/<int:meal_id>', views.delete_meal, name="delete_meal"),
    path('edit-meal/<int:meal_id>', views.edit_meal, name="edit_meal"),
    path('calculate_bmi', views.calculate_bmi, name="calculate_bmi"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/signup/", user_views.SignUpView.as_view(), name="signup"),

]
