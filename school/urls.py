# C:\Users\USER\Desktop\sms\Home\school\urls.py

from django.urls import path
from . import views # Import the view functions from the same directory

# The urlpatterns list is essential for the server to run correctly.
urlpatterns = [
    # When a request comes to the root of the app ('/'), call the 'index' function 
    # defined in school/views.py.
    path('', views.index, name='index'), 
]