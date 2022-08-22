from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, post, category

urlpatterns = [
    path('',home),
    path('blog/<slug:url>',post),
    path('category/<slug:url>',category)
]