from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class TicketType(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    status = models.BooleanField(default=True)
    img_url = models.URLField(null=True, blank=True)


# Ticket reference
class Ticket(models.Model):
    """
    Ticket created by user linked to a TicketType docuemnt
    """

    STATE = [('SEND', 'Sended'), ('START', 'Started'), ('WAIT', 'Lavoration'), ('BUSY', 'Document Wait'),
        ('COMP', 'Complete'), ('TRASH', 'Eliminated'),

    ]

    title = models.CharField(max_length=80)
    description = models.CharField(max_length=250)

    client = models.ForeignKey(User, on_delete=models.SET(f'{User.username}'), related_name='cleint')
    type_document = models.ForeignKey(TicketType, on_delete=models.PROTECT, related_name='ticket_type')

    status = models.CharField(choices=STATE, max_length=5)
    status_bool = models.BooleanField(default=True)  # for close ticket
    date_create = models.DateTimeField(auto_now_add=True)
    date_close = models.DateTimeField(blank=True, null=True)
    date_last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.type_document.title} | {self.client}'

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"


# Ticket reference
class TicketField(models.Model):
    """
    Ticket field for ticket
    """

    lable = models.CharField(max_length=60)
    value = models.CharField(max_length=60, blank=True, null=True)

    ticket_type = models.ForeignKey(Ticket, on_delete=models.PROTECT, related_name="ticket_field")

    def __str__(self):
        return f'{self.ticket_type.pk} - {self.ticket_type.title} | {self.lable}'


# TicketType reference
class FieldInputText(models.Model):
    """
    Models for Input Field class in HTML
    """

    index = models.IntegerField()
    lable = models.CharField(max_length=60)

    placeholder = models.CharField(max_length=60, blank=True, null=True)
    value = models.CharField(max_length=60, blank=True, null=True)
    max_lenght = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(250)])
    min_lenght = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(249)])
    ticket_type = models.ForeignKey(TicketType, on_delete=models.CASCADE, related_name="ticket_type_inputtext")

    def __str__(self):
        return f'{self.ticket_type.title} | {self.lable}'


# TicketType reference
class FieldTextArea(models.Model):
    """
    Models for Textarea class in HTML
    """

    index = models.IntegerField()
    lable = models.CharField(max_length=60)

    placeholder = models.CharField(max_length=100, null=True, blank=True)
    value = models.CharField(max_length=100, null=True, blank=True)

    rows = models.IntegerField(default=6)
    cols = models.IntegerField(default=40)

    max_lenght = models.IntegerField(validators=[MinValueValidator(1)], null=True, blank=True)
    min_lenght = models.IntegerField(validators=[MinValueValidator(0)], null=True, blank=True)

    ticket_type = models.ForeignKey(TicketType, on_delete=models.CASCADE, related_name="ticket_type_textarea")

    def __str__(self):
        return f'{self.ticket_type.title} | {self.lable}'


# TicketType reference
class FieldCeckBox(models.Model):
    """
    Models for Textarea class in HTML
    """
    index = models.IntegerField()
    lable = models.CharField(max_length=60)

    default = models.BooleanField(default=False)
    value = models.CharField(max_length=60, blank=True, null=True)

    ticket_type = models.ForeignKey(TicketType, on_delete=models.CASCADE, related_name="ticket_type_field_ceckbox")

    def __str__(self):
        return f'{self.ticket_type.title} | {self.lable}'


# TicketType reference
class GroupRadioButton(models.Model):
    """
    Models for Cotainer of Radiobutton imput class in HTML
    """

    index = models.IntegerField()
    lable = models.CharField(max_length=60)

    ticket_type = models.ForeignKey(TicketType, on_delete=models.CASCADE, related_name="ticket_type_radiogroup")

    def __str__(self):
        return f'{self.ticket_type.title} | {self.lable}'


# TicketType reference
class ElementRadio(models.Model):
    """
    Models for Radiobutton for Container row
    """

    lable = models.CharField(max_length=60)
    value = models.CharField(max_length=60)

    input_group = models.ForeignKey(GroupRadioButton, on_delete=models.CASCADE, related_name="input_group_radiogroup")

    def __str__(self):
        return f'{self.input_group.lable} | {self.lable}'


# TicketType reference
class GroupDropDown(models.Model):
    """
    Models for Cotainer of DrowpDown menu imput class in HTML
    """

    index = models.IntegerField()
    lable = models.CharField(max_length=60)

    ticket_type = models.ForeignKey(TicketType, on_delete=models.CASCADE, related_name="ticket_type_dropdown")

    def __str__(self):
        return f'{self.ticket_type.title} | {self.lable}'


# TicketType reference
class ElementDropDown(models.Model):
    """
    Models for DrowpDown for Group row
    """

    lable = models.CharField(max_length=60)
    value = models.CharField(max_length=60)

    input_group = models.ForeignKey(GroupDropDown, on_delete=models.CASCADE, related_name="input_group_dropdown")

    def __str__(self):
        return f'{self.input_group.lable} | {self.lable}'


# TicketType reference
class GroupCeckBox(models.Model):
    """
    Models for CeckBox for Group row
    """

    index = models.IntegerField()
    lable = models.CharField(max_length=60)

    ticket_type = models.ForeignKey(TicketType, on_delete=models.CASCADE, related_name="ticket_type_ceckbox")

    def __str__(self):
        return f'{self.ticket_type.title} | {self.lable}'


# TicketType reference
class ElementCeckBox(models.Model):
    """
    Models for CeckBox for Group row
    """

    lable = models.CharField(max_length=60)
    value = models.CharField(max_length=60)

    input_group = models.ForeignKey(GroupCeckBox, on_delete=models.CASCADE, related_name="input_group_ceckbox")

    def __str__(self):
        return f'{self.input_group.lable} | {self.lable}'
