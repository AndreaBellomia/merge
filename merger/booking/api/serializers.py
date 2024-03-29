from rest_framework import serializers

from ..models import Appointments, Booking


class AppointmentsSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source="owner.username", read_only=True)

    class Meta:
        model = Appointments
        fields = "__all__"

    # validate date and time of prenotation
    def validate_data(self, value):
        if value['start_time'] > value['end_time']:
            raise serializers.ValidationError(
                {"detail": f"DATA Time errors - Date not allow {value['start_time']} and later {value['end_time']}"})
        return True


class BookingSerializer(serializers.ModelSerializer):
    commiter = serializers.CharField(source="commiter.username", read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ('start_time', 'end_time', 'state', 'available', 'commiter')

    # def validate(self, data):
    #     """
    #     Check that start is before finish.
    #     """
    #     if data["start_time"] > data["end_time"]:
    #         raise serializers.ValidationError({"detail": f"DATA Time errors - Date not allow {data['start_time']} and later {data['end_time']}"})
    #     return True
