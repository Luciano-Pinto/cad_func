from django.shortcuts import render


def home(request):
    return render(request, 'cad_func/home.html')