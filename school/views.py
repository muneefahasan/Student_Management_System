# C:\Users\USER\Desktop\sms\Home\school\views.py

from django.http import HttpResponse

def index(request):
    """
    Handles requests to the school app's index page.
    """
    return HttpResponse("Hello, Django! This is the school app working correctly.")