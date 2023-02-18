from rest_framework     import serializers
from ticket.models      import Ticket, TicketType



class TicketsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = "__all__"

class TicketsTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = TicketType
        fields = "__all__"