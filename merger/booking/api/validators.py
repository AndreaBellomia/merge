
from rest_framework     import serializers
from django.utils       import timezone



class BookingValidator():
    """"
    Class for validate a booking creation
    """

    def __init__(self, appointment):
        self.appointment = appointment

    def ValidateAppBooking(self):
        if timezone.now() >= self.appointment.start_time:
            raise serializers.ValidationError({"detail": f"DATA Time errors - Date not allow current:{timezone.now()} and later {self.appointment.start_time}"})
        
        if self.appointment.state != 'FREE':
            raise serializers.ValidationError({"detail": f"State errors - this appointment is not currently available"})
        return True
    