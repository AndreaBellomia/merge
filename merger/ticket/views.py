from ticket.models              import Ticket, TicketType
from ticket.api.serializers     import TicketsSerializer, TicketsTypeSerializer

from django.shortcuts           import get_object_or_404
from django.utils               import timezone

from rest_framework             import generics, status
from rest_framework.views       import APIView
from rest_framework.response    import Response




class TicketApiView(generics.ListCreateAPIView):

    serializer_class = TicketsSerializer

    def get_queryset(self):
        """
        This view should return a list of all ticket
        for the currently authenticated user.
        """
        user = self.request.user
        return Ticket.objects.filter(cliente=user)
    

class TicketTipeApiView(generics.ListAPIView):

    queryset = TicketType.objects.all()
    serializer_class = TicketsTypeSerializer