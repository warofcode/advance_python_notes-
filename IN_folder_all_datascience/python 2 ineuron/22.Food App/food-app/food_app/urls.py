from django.contrib import admin
from django.urls import path, include
from food import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('food.urls')),
]
