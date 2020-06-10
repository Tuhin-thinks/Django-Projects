from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    # if request.POST.get('click', False):
    #     self.registration(request)
    # return render(request, 'bookings/home.html')
    if request.method == 'GET':
        return render(request, 'bookings/home.html')
    elif request.method == 'POST':
        return render(request, 'bookings/admin.html')

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

def new_menber(request):
    # if request.POST.get('click', False):
    #     self.registration(request)
    # return render(request, 'bookings/admin.html')
    if request.method == 'GET':
        return render(request, 'bookings/new_member.html')
    elif request.method == 'POST':
        return render(request, 'bookings/new_member.html')
    return render(request, 'bookings/new_member.html') # /templates/booking/bookings/new_menber.html
