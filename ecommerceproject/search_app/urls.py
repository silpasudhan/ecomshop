from . import views
from django.urls import path, include
app_name='search_app'
urlpatterns = [

    path('', views.SearchResult, name='SearchResult'),

]
