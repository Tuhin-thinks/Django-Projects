from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def login(request):
    # if request.POST.get('click', False):
    #     self.registration(request)
    # return render(request, 'bookings/login.html')
    if request.method == 'GET':
        return render(request, 'bookings/login.html')
    elif request.method == 'POST':
        return render(request, 'bookings/login.html')

def administration(request):
    # if request.POST.get('click', False):
    #     self.registration(request)
    # return render(request, 'bookings/admin.html')
    if request.method == 'GET':
        return render(request, 'bookings/administration.html')
    elif request.method == 'POST':
        return render(request, 'bookings/administration.html')

def registration(request):
    # if request.POST.get('click', False):
    #     self.registration(request)
    # return render(request, 'bookings/registration.html')
    if request.method == 'GET':
        return render(request, 'bookings/registration.html')
    elif request.method == 'POST':
        return render(request, 'bookings/admin.html')
    return render(request, 'bookings/registration.html') # /templates/booking/bookings/registration.html

def admin(request):
    # if request.POST.get('click', False):
    #     self.registration(request)
    # return render(request, 'bookings/admin.html')
    if request.method == 'GET':
        return render(request, 'bookings/admin.html')
    elif request.method == 'POST':
        return render(request, 'bookings/admin.html')
    return render(request, 'bookings/admin.html') # /templates/booking/bookings/admin.html

def new_member(request):
    # if request.POST.get('click', False):
    #     self.registration(request)
    # return render(request, 'bookings/new_member.html')
    if request.method == 'GET':
        return render(request, 'bookings/new_member.html')
    elif request.method == 'POST':
        return render(request, 'bookings/new_member.html')
    return render(request, 'bookings/new_member.html') # /templates/booking/bookings/new_member.html

def forgot_password(request):
    # if request.POST.get('click', False):
    #     self.registration(request)
    # return render(request, 'bookings/forgot_password.html')
    if request.method == 'GET':
        return render(request, 'bookings/forgot_password.html')
    elif request.method == 'POST':
        return render(request, 'bookings/forgot_password.html')
    return render(request, 'bookings/forgot_password.html') # /templates/booking/bookings/forgot_password.html

def change_password(request):
    # if request.POST.get('click', False):
    #     self.registration(request)
    # return render(request, 'bookings/change_password.html')
    if request.method == 'GET':
        return render(request, 'bookings/change_password.html')
    elif request.method == 'POST':
        return render(request, 'bookings/change_password.html')
    return render(request, 'bookings/change_password.html') # /templates/booking/bookings/change_password.html