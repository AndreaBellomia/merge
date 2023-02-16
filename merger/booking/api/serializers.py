from rest_framework     import serializers
from booking.models     import Appointments, Booking




class AppointmentsSerializer(serializers.ModelSerializer):

    

    class Meta:
        model = Appointments

        fields = "__all__"

    #validate date and time of prenotation
    def validate_data(self, value):
        if value['start_time'] > value['end_time']:
            raise serializers.ValidationError({"detail": f"DATA Time errors - Date not allow {value['start_time']} and later {value['end_time']}"})
        return True
    

class BookingSerializer(serializers.ModelSerializer):

    appointments = serializers.StringRelatedField()



    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ('start_time', 'end_time', 'stato', 'abilitato', 'commiter')

    # def validate(self, data):
    #     """
    #     Check that start is before finish.
    #     """
    #     if data["start_time"] > data["end_time"]:
    #         raise serializers.ValidationError({"detail": f"DATA Time errors - Date not allow {data['start_time']} and later {data['end_time']}"})
    #     return True
