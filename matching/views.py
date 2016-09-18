from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context)

def questions(request):
    context = {}
    return render(request, 'questions.html', context)

def login(request):
    context = {}
    return render(request, 'login.html', context)

def userpage(request):
    context = {}
    return render(request, 'userpage.html', context)

def swipeSupply(request):
    context = {}
    return render(request, 'swipe_supply.html', context)

def dashboard(request):
    context = {}
    return render(request, 'dashboard.html', context)

def matchesDashboard(request):
    context = {}
    return render(request, 'matches_dashboard.html', context)