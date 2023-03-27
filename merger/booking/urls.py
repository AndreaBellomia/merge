from django.urls import path

from .views import AppointmentsListApiView, AppointmentDatailApiView, BookingApiView, BookingUpdateDeleteApiView

urlpatterns = [
    path('client/appointments/',
         AppointmentsListApiView.as_view(),
         name='pre-boking-list'),

    path('client/appointments/<int:pk>',
         AppointmentDatailApiView.as_view(),
         name='pre-boking'),

    path('client/booking/',
         BookingApiView.as_view(),
         name='list-booking'),

    path('client/booking/<int:pk>',
         BookingUpdateDeleteApiView.as_view(),
         name='meke-booking'),
]
