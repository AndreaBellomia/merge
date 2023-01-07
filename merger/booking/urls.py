from django.urls import path

from booking.views import AppointmentsListApiView, AppointmentDatailApiView, BookingApiView, BookingUpdateDeleteApiView


urlpatterns = [
    path('appointments/', 
        AppointmentsListApiView.as_view(), 
        name='pre-boking-list'),
    
    path('appointments/<int:pk>', 
        AppointmentDatailApiView.as_view(), 
        name='pre-boking'),
    
    path('booking/', 
        BookingApiView.as_view(), 
        name='list-booking'),
    
    path('booking/<int:pk>', 
        BookingUpdateDeleteApiView.as_view(), 
        name='meke-booking'),
]