from django.urls import path
from news_app import views

urlpatterns = [
    path('',views.index,name="news_app"),
]