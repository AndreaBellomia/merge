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
    queryset = Ticket.objects.filter()


# class TicketApiView(APIView):


#     def get_object(self):
#         user = self.request.user
#         return Ticket.objects.filter(client=user)

#     def get(self, request):
#         instace = self.get_object()
#         serializer = TicketsSerializer(instace, many=True)
#         return Response(serializer.data) 
    
#     def post(self, request):
#         print(request.data)
#         serializer = TicketsSerializer()
#         print(serializer)
#         return Response('serializer.data', status=status.HTTP_201_CREATED)


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



