from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='login'), # this is for home
    path('admin/', views.admin), # this is for admin panel
    path('registration/', views.registration), # this is for registration now you have to add for login/
    path('new_member/', views.registration)
    path('forgot_password/', views.registration)
    path('change_password/', views.registration)


    # these whole functions
]
