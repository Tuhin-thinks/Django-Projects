from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('posts/<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('contact', views.contact, name='contact'),

]
