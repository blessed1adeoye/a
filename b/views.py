from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def home(request):
    hi = HomE.objects.all()
    context = {
        'ade': 'home',
        'hi': hi
    }
    return render(request, 'b/home.html', context)



def about (request):
    abt = About.objects.all()
    context = {
        'nav': 'about',
        'abt': abt
    }
    return render(request, 'b/about.html', context)


def educate(request):
    me = Education.objects.all()

    context = {
        'nav': 'educate',
        'me': me
    }
    
    return render(request, 'b/edu.html', context)


def port(request):
    abd = Portfolio.objects.all()

    context = {
        'nav': 'port',
        'abd': abd
    }
    return render(request, 'b/port.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        c = Contact(name=name, email=email, subject=subject, message=message)
        c.save()
        messages.success(request, f'We receive your message and we will get back to you on {email}, as soon as possible')
        return redirect('b:contact')
    context = {
        'nav': 'contact',
    }
    
    return render(request, 'b/contact.html', context)



