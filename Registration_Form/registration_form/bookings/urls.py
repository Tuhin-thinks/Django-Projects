from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'), # this is for home
    path('admin/', views.admin), # this is for admin panel
    path('registration/', views.registration), # this is for registration now you have to add for login/
    # these whole functions
]
