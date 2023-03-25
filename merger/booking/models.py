from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Appointments(models.Model):
    """
    Model that contain dates for user by admin
    """
    STATE = [('FREE', 'Available'), ('WAIT', 'Wait'), ('BLOCK', 'Booked')]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    active = models.BooleanField(default=True)
    state = models.CharField(choices=STATE, max_length=5)

    def __str__(self):
        return self.owner.username + '|' + str(self.start_time)

    class Meta:
        verbose_name = "Appointment"
        verbose_name_plural = "Appointments"


class Booking(models.Model):
    """
    Model that contain appointments
    """

    STATE = [('FREE', 'Available'), ('WAIT', 'Wait'), ('BUSY', 'Booked'), ('BLOCK', 'Blocked'),
             ('PAUSE', 'Suspended'), ]

    description = models.CharField(max_length=240)
    type = models.CharField(max_length=50)

    state = models.CharField(choices=STATE, max_length=5)
    available = models.BooleanField(default=True)

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    prenotation_time = models.DateTimeField(auto_now_add=True)

    appointments = models.ForeignKey(Appointments, on_delete=models.CASCADE)
    commiter = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=None)

    def __str__(self):
        return str(self.appointments.owner.username) + ' | ' + self.commiter.username + ' - ' + str(
            self.appointments.start_time)

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
