# Application Import
# Django Import
from django.shortcuts import get_object_or_404
# Rest Framework import
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .api.serializers import TicketTypeSerializer, TicketTypeRelatedSerializer, TicketsSerializer
from .models import Ticket, TicketType


class TicketApiView(APIView):

    def get(self, request):
        query_instace = Ticket.objects.filter()
        serializer = TicketsSerializer(query_instace, many=True)
        return Response(serializer.data)

    def post(self, request):

        request.data["status"] = "SEND"
        request.data["client"] = request.user.id

        serializer = TicketsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TicketTypeDatailApiView(APIView):
    """
    ApiView for TicketType with related fields
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
