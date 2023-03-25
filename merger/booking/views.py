# Create your views here.
# Application Import
# Django Import
from django.shortcuts import get_object_or_404
from django.utils import timezone
# Rest Framework import
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

# Other Library Import
from .api.serializers import AppointmentsSerializer, BookingSerializer
from .api.validators import BookingValidator
from .models import Appointments, Booking


class AppointmentsListApiView(APIView):
    """
    EndPoints Return a list of appointments and add new appointment
    """

    def get(self, request):
        query_instace = Appointments.objects.filter(start_time__gte=timezone.now(), state='FREE')
        serializer = AppointmentsSerializer(query_instace, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AppointmentsSerializer(data=request.data)
        if serializer.is_valid() and serializer.validate_data(request.data):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AppointmentDatailApiView(APIView):
    """
    EndPoints Return a specific appointment update and delete one
    """

    def get_object(self, pk):
        query = get_object_or_404(Appointments, pk=pk)
        return query

    def get(self, request, pk):
        instance = self.get_object(pk)
        serializer = AppointmentsSerializer(instance)
        return Response(serializer.data)

    def put(self, request, pk):
        instance = self.get_object(pk)
        serializer = AppointmentsSerializer(instance, data=request.data)
        if serializer.is_valid() and serializer.validate(data=request.data):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        instance = self.get_object(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookingApiView(generics.ListCreateAPIView):
    """
    EndPoints Return list of booking and create new one
    """
    serializer_class = BookingSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Booking.objects.filter(commiter=user, start_time__gte=timezone.now())

    def perform_create(self, serializer):
        """
        Manage the Creating mixin for auto compile the readonly filds
        """

        instace = Appointments.objects.get(pk=self.request.data['appointments'])
        if BookingValidator(instace).validate_app_booking():
            instace.state = 'WAIT'
            instace.save()
            serializer.save(start_time=instace.start_time, end_time=instace.end_time, state='WAIT',
                            commiter=self.request.user, appointments=instace)


class BookingUpdateDeleteApiView(APIView):
    """
    EndPoints Return update and delete sigle booking
    """

    def get_object(self, pk):
        query = get_object_or_404(Booking, pk=pk)
        return query

    def get(self, request, pk):
        instance = self.get_object(pk)
        if instance.available:
            serializer = BookingSerializer(instance)
            return Response(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        instance = self.get_object(pk)
        serializer = BookingSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        instance = self.get_object(pk)
        serializer = BookingSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        instance = self.get_object(pk)
        if instance.state in ['FREE', 'WAIT']:
            instance.appointments.state = 'FREE'
            instance.appointments.save()
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_304_NOT_MODIFIED)
