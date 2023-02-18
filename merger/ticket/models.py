from django.db import models
from django.contrib.auth.models import User



class TicketType(models.Model):
    """
    Models per la creazione dei tipi di ticket
    """

    title = models.CharField(max_length=80)
    description = models.CharField(max_length=250)
    active = models.BooleanField(default=True)
    img_url =  models.URLField(blank=True)

    def __str__(self):
        return f'{self.title} | {self.active}'
    
    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"
    



class Ticket(models.Model):

    """
    Ticket centralizzato per la gerstione delle varie implementaqzioni
    """

    STATO = [
        ('SEND', 'Sended'),
        ('START', 'Started'),
        ('WAIT', 'Lavoration'),
        ('BUSY', 'Document Wait'),
        ('COMP', 'Complete'),
        ('TRASH', 'Eliminated'),

    ]

    type_document = models.ForeignKey(TicketType, on_delete=models.SET(f'{TicketType.title}'), related_name='ticket')
    cliente = models.ForeignKey(User, on_delete=models.SET(f'{User.username}'), related_name='cliente')
    description = models.CharField(max_length=250)
    object = models.CharField(max_length=80)
    status = models.CharField(choices=STATO, max_length=5)
    status_bool = models.BooleanField(default=True) # for close ticket

    date_create = models.DateTimeField(auto_now_add=True)
    date_close = models.DateTimeField(blank=True, null=True)
    date_last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.type_document.title} | {self.cliente}'
    
    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"
    


class TicketMsg(models.Model):
    """
    Chat dedicata al ticket centrrralizzato
    """
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='msg')
    autor = models.ForeignKey(User, on_delete=models.SET(f'{User.username}'), related_name='client')
    message = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.autor} | {self.date_create}'
    
    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"

