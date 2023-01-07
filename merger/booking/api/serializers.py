from rest_framework import serializers
from booking.models import Appointments, Booking
from django .utils import timezone




class AppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = "__all__"

    def validate(self, data):
        """
        Check that start is before finish.
        """
        if data["start_time"] > data["end_time"]:
            raise serializers.ValidationError({"detail": f"DATA Time errors - Date not allow {data['start_time']} and later {data['end_time']}"})
        return True

    

class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ('start_time', 'end_time', 'stato', 'abilitato')

    # def validate(self, data):
    #     """
    #     Check that start is before finish.
    #     """
    #     if data["start_time"] > data["end_time"]:
    #         raise serializers.ValidationError({"detail": f"DATA Time errors - Date not allow {data['start_time']} and later {data['end_time']}"})
    #     return True
