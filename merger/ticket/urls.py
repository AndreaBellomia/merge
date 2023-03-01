from django.urls import path
from ticket.views import TesetView, TicketTypeDatailApiView, TicketTypeView, TicketApiView


urlpatterns = [
    path('ticket', TesetView.as_view(), name='ticket'),

    path('client/ticket-type/<int:pk>', 
         TicketTypeDatailApiView.as_view(), 
         name='ticket_type_datail'),
    
    path('client/ticket-type/', 
         TicketTypeView.as_view(), 
         name='ticket_type_datail'),

    path('client/tickets/', 
        TicketApiView.as_view(), 
        name='ticket_list'),


]