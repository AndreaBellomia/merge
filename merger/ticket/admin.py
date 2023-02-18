from django.contrib import admin

from ticket.models import Ticket, TicketType, TicketMsg

# Register your models here.



admin.site.register(Ticket)
admin.site.register(TicketType)
admin.site.register(TicketMsg)