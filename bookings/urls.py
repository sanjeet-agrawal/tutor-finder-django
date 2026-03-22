from django.urls import path
from . import views

urlpatterns = [
    path('book/<int:tutor_id>/', views.book_tutor, name='book_tutor'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('tutor-bookings/', views.tutor_bookings, name='tutor_bookings'),
]