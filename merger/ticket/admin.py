from django.contrib import admin

from .models import *

# Register your models here.

DECLARED_FIELDS = (
TicketType, Ticket, TicketField, FieldInputText, FieldTextArea, FieldCeckBox, GroupRadioButton, ElementRadio,
GroupDropDown, ElementDropDown, GroupCeckBox, ElementCeckBox)

for model in DECLARED_FIELDS:
    admin.site.register(model)
