from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePage.as_view(), name="home"),
    path('<int:pk>/', views.DetailPage.as_view(), name="detail"),
    path("navigate/", views.news, name="news")
]