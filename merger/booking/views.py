# Application Import 
from booking.models             import Appointments, Booking
from booking.api.serializers    import AppointmentsSerializer, BookingSerializer
from booking.api.validators     import BookingValidator

# Django Import 
from django.shortcuts           import get_object_or_404
from django.utils               import timezone

# Rest Frameword import
from rest_framework             import generics, status
from rest_framework.views       import APIView
from rest_framework.response    import Response


# Other Library Import 





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
        instace = self.get_object(pk)
        serializer = AppointmentsSerializer(instace)
        return Response(serializer.data)    

    def put(self, request, pk):
        instace = self.get_object(pk)
        serializer = AppointmentsSerializer(instace, data=request.data)
        if serializer.is_valid() and serializer.validate(data=request.data):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        instace = self.get_object(pk)
        instace.delete()
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
        query = serializer.validated_data['appointments']
        instace = Appointments.objects.get(pk=self.request.data['appointments'])
        if BookingValidator(instace).ValidateAppBooking():
            instace.state='WAIT'
            instace.save()
            serializer.save(start_time=query.start_time, 
                            end_time=query.end_time,
                            stato='WAIT',
                            commiter=self.request.user)



class BookingUpdateDeleteApiView(APIView):
    """
    EndPoints Return update and delete sigle booking
    """


    def get_object(self, pk):
        query = get_object_or_404(Booking, pk=pk)
        return query
    
    def get(self, request, pk):
        instace = self.get_object(pk)
        if instace.abilitato:
            serializer = BookingSerializer(instace)
            return Response(serializer.data)  
        return Response(status=status.HTTP_204_NO_CONTENT)          

    def patch(self, request, pk):
        instace = self.get_object(pk)
        serializer = BookingSerializer(instace, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        instace = self.get_object(pk)
        serializer = BookingSerializer(instace, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        instace = self.get_object(pk)
        if instace.stato in ['FREE', 'WAIT']:
            instace.appointments.state = 'FREE'
            instace.appointments.save()
            instace.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_304_NOT_MODIFIED)
