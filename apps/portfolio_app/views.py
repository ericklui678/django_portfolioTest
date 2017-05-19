from django.shortcuts import render, redirect

def index(request):
    return render(request, 'portfolio_app/index.html')

def testimonials(request):
    return render(request, 'portfolio_app/testimonials.html')
