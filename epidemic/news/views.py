from django.shortcuts import render

# Create your views here.
def mysql(request):

    return render(request, "mysql.html")

def index(request):

    return render(request, "index.html")

def about(request):

    return render(request, "about.html")