# C:\Users\USER\Desktop\sms\Home\Home\urls.py

from django.contrib import admin
from django.urls import path, include # 'include' MUST be imported here

urlpatterns = [
    # The default path for the Django Admin interface
    path('admin/', admin.site.urls),
    
    # This line tells Django to include all URLs defined in the 'school' app's urls.py
    path('', include("school.urls")), 
]