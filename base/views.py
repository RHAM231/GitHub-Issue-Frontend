from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'base/home.html')


def ms_index(request):
    return render(request, 'base/ms_index.html')