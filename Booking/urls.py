from django.urls import path
from . import views

app_name = 'Booking'

urlpatterns = [
    path('table/', views.TableBooking, name='table'),
]
