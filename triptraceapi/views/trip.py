from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from triptraceapi.models import Trip, User

class TripView(ViewSet):
    """Trip View"""
    def retrieve(self, request, pk):
        try:
            trip = Trip.objects.get(pk=pk)
            serializer = TripSerializer(trip)
            return Response(serializer.data)
        except Trip.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        trips = Trip.objects.all()
        
        public = self.request.query_params.get("public", None)
        if public is not None:
            trips = trips.filter(public=public)
            
        traveler_id = self.request.query_params.get("traveler_id", None)
        if traveler_id is not None:
            trips = trips.filter(traveler_id=traveler_id)

        serializer = TripSerializer(trips, many=True)
        return Response(serializer.data)
      
    def create(self, request):
        traveler = User.objects.get(id=request.data["traveler_id"])
        trip = Trip.objects.create(
            traveler=traveler,
            title=request.data["title"],
            description=request.data["description"],
            image_url=request.data["image_url"],
            created_on=request.data["created_on"],
            duration=request.data["duration"],
            duration_unit=request.data["duration_unit"],
            region=request.data["region"],
            country=request.data["country"],
            city=request.data["city"],
            public=request.data["public"],
            price_range=request.data["price_range"]
          )
        serializer = TripSerializer(trip)
        return Response(serializer.data)
    
    def update(self, request, pk):
        trip = Trip.objects.get(pk=pk)
        trip.title = request.data["title"]
        trip.description = request.data["description"]
        trip.image_url = request.data["image_url"]
        trip.duration = request.data["duration"]
        trip.duration_unit = request.data["duration_unit"]
        trip.region = request.data["region"]
        trip.country = request.data["country"]
        trip.city = request.data["city"]
        trip.public = request.data["public"]
        trip.price_range = request.data["price_range"]
        trip.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk):
        """Handle DELETE requests for a single post"""
        trip = Trip.objects.get(pk=pk)
        trip.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class TripSerializer(serializers.ModelSerializer):
    """serializer for trips"""
    created_on = serializers.DateTimeField()
    class Meta:
        model = Trip
        depth = 1
        fields = ('id', 'title', 'description', 'image_url', 'created_on', 'duration', 'duration_unit', 'traveler_id', 'region', 'country', 'city', 'public', 'price_range')
