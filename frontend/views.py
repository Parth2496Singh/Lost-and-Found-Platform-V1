from django.shortcuts import render

# Create your views here.


def index(request):
    print("INDEX VIEW CALLED")
    return render(request, 'home.html')

# Temporary placeholders for other pages
def report_lost(request):
    print("REPORT LOST VIEW CALLED")
    return render(request, 'report_lost.html')

def report_found(request):
    return render(request, 'report_found.html')

def search(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'dashboard.html')


def lost_detail(request, id):
    return render(request, "lost_detail.html", {"id": id})

def found_detail(request, id):
    return render(request, "found_detail.html", {"id": id})


def privacy_policy(request):
    return render(request, "privacy_policy.html")

def terms_of_service(request):
    return render(request, "terms_of_service.html")
