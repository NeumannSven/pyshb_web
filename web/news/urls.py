from django.urls import path
from . import views

urlpatterns = [
    path('', views.showWebSite),
    path('main/', views.main),
    path('articles/', views.showArticles),
]