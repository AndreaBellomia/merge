from django.urls import path

from ticket.views import TicketApiView, TicketTipeApiView



urlpatterns = [
    path('client/tickets/', 
        TicketApiView.as_view(), 
        name='ticket-list'),

    path('client/ticket-tipe/', 
        TicketTipeApiView.as_view(), 
        name='ticket-type-list'),
]