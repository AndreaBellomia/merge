from django.contrib import admin

from ticket.models import Ticket, TicketTipe, TicketCommit, TicketMsg

# Register your models here.



admin.site.register(Ticket)
admin.site.register(TicketTipe)
admin.site.register(TicketCommit)
admin.site.register(TicketMsg)