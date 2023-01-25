from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from triptraceapi.models import Stop, Trip, Country

class StopView(ViewSet):
    """Stop View"""
    def retrieve(self, request, pk):
        try:
            stop = Stop.objects.get(pk=pk)
            serializer = StopSerializer(stop)
            return Response(serializer.data)
        except Stop.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        stops = Stop.objects.all()
        trip_id = self.request.query_params.get("trip_id", None)
        if trip_id is not None:
            stops = stops.filter(trip_id=trip_id)

        serializer = StopSerializer(stops, many=True)
        return Response(serializer.data)
      
    def create(self, request):
        trip = Trip.objects.get(id=request.data["trip_id"])
        country = Country.objects.get(id=request.data["country_id"])
        stop = Stop.objects.create(
            trip=trip,
            title=request.data["title"],
            country=country,
            city=request.data["city"],
            duration=request.data["duration"],
            duration_unit=request.data["duration_unit"],
            price_range=request.data["price_range"]
          )
        serializer = StopSerializer(stop)
        return Response(serializer.data)
    
    def update(self, request, pk):
        stop = Stop.objects.get(pk=pk)
        country = Country.objects.get(id=request.data["country"]["id"])
        stop.title = request.data["title"]
        stop.duration = request.data["duration"]
        stop.duration_unit = request.data["duration_unit"]
        stop.country = country
        stop.city = request.data["city"]
        stop.price_range = request.data["price_range"]
        stop.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk):
        """Handle DELETE requests for a single post"""
        stop = Stop.objects.get(pk=pk)
        stop.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class StopSerializer(serializers.ModelSerializer):
    """serializer for stops"""
    class Meta:
        model = Stop
        depth = 2
        fields = ('id', 'trip', 'title', 'country', 'city', 'duration', 'duration_unit', 'price_range')
