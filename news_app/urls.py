from django.urls import path
from news_app.views import index,search,pop_database

app_name = 'news_app'

urlpatterns = [
    path('',index,name="index"),
    path('search/',search,name="search"),
    path('pop_database/',pop_database,name="pop_database"),
]