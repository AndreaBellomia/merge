from django.contrib import admin

from ticket.models import *

DECLARED_FIELDS = (TicketType, Ticket, TicketField, FieldInputText, FieldTextArea, FieldCeckBox, GroupRadioButton, ElementRadio, GroupDropDown, ElementDropDown, GroupCeckBox, ElementCeckBox)

# Register your models here.




for model in DECLARED_FIELDS:
    admin.site.register(model)

