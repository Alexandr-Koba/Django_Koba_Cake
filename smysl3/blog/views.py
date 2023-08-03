from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse('<html><title>Koba Cake</title><h1>Koba Cake - Закажи десерт</h1></http>')
