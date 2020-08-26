from django.urls import path
from .views import blogview,single_view,category_view,search
urlpatterns = [
    
    path('',blogview,name='home'),
    path('post/<str:slug>/',single_view,name='post'),
    path('category/<str:name>/',category_view,name='category'),
    path('search/',search,name='search')
]
