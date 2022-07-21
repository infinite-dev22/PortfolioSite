from django.urls import path
from .views import indexView, successView

app_name= 'Portifolio'

urlpatterns = [
    path('', indexView, name='home'),
    path('successful/', successView, name='success'),
]