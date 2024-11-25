from django.urls import path
from . import views
from bar_project import settings
from django.conf.urls.static import static


urlpatterns = [
    path('book/', views.book_table, name='book_table'),
    path('manager/', views.booking_manager, name='booking_manager'),
    path('my-bookings/', views.user_bookings, name='user_bookings'),
    path('menu/', views.menu_view, name='menu'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
