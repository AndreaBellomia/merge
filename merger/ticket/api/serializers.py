from rest_framework     import serializers
from ticket.models      import Ticket, TicketType

class TicketsTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = TicketType
        fields = "__all__"
class TicketsSerializer(serializers.ModelSerializer):

    type_document = serializers.PrimaryKeyRelatedField(read_only=True)
    type_document = TicketsTypeSerializer(type_document)
    class Meta:
        model = Ticket
        fields = "__all__"

