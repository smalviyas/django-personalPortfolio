from django.urls import path
from django.urls.resolvers import URLPattern
from .views import blog, detail
app_name = 'blog'
urlpatterns =[
    path('',blog, name='blog'),
    path('<int:blog_id>' ,detail , name='detail')
]