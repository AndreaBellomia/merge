# Application Import 
from ticket.models              import Ticket, TicketType
from ticket.api.serializers     import TicketTypeSerializer, TicketTypeRelatedSerializer, TicketsSerializer

# Django Import 
from django.shortcuts           import get_object_or_404

# Rest Frameword import
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

class TicketTypeDatailApiView(APIView):
    """
    ApiView fror TicketType with related fields
    """

    def get_object(self, pk):
        query = get_object_or_404(TicketType, pk=pk)
        return query

    def get(self, request, pk):
        instace = self.get_object(pk)
        serializer = TicketTypeRelatedSerializer(instace)
        return Response(serializer.data)    


class TicketTypeView(generics.ListAPIView):
    serializer_class = TicketTypeSerializer
    queryset = TicketType.objects.all()



class TesetView(generics.ListAPIView):
    serializer_class = TicketTypeSerializer
    queryset = TicketType.objects.all()



