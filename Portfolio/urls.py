from django.urls import path
from .views import indexView, successView

app_name= 'Portfolio'

urlpatterns = [
    path('', indexView, name='home'),
    path('successful/', successView, name='success'),
]