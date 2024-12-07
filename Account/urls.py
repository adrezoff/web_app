from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = 'Account'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/update/', views.profile_update_view, name='profile_update'),
    path('logout/', views.logout_view, name='logout'),
    path('accounts/login/', RedirectView.as_view(url='/account/login/')),
    path('cancel_booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]
