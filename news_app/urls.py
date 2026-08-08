from django.urls import path
from news_app.views import index,search

app_name = 'news_app'

urlpatterns = [
    path('',index,name="index"),
    path('search/',search,name="search"),
]