from django.shortcuts import render, redirect
from whiteApp.models import ContactForm


def home(request):
    return render(request, 'home1.html')


def order(request):
    return render(request, 'order-now.html')


def form(request):
    name = request.POST['name']
    company = request.POST['company']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']

    contact = ContactForm(name=name, company=company, email=email, phone=phone, message=message)
    contact.save()
    return redirect('/')
