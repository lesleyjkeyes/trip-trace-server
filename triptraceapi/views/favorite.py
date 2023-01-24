from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from triptraceapi.models import Favorite, User, Trip

class FavoriteView(ViewSet):
    """Favorite View"""
    def retrieve(self, request, pk):
        try:
            favorite = Favorite.objects.get(pk=pk)
            serializer = FavoriteSerializer(favorite)
            return Response(serializer.data)
        except Favorite.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        favorites = Favorite.objects.all()
        traveler_id = self.request.query_params.get("traveler_id", None)
        if traveler_id is not None:
            favorites = favorites.filter(traveler_id=traveler_id)
        serializer = FavoriteSerializer(favorites, many=True)
        return Response(serializer.data)
      
    def create(self, request):
        traveler = User.objects.get(id=request.data["traveler_id"])
        trip = Trip.objects.get(id=request.data["trip_id"])
        favorite = Favorite.objects.create(
            traveler = traveler,
            trip = trip
          )
        serializer = FavoriteSerializer(favorite)
        return Response(serializer.data)

    def delete(self, request, pk):
        """Handle DELETE requests for a single favorite"""
        favorite = Favorite.objects.get(pk=pk)
        favorite.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class FavoriteSerializer(serializers.ModelSerializer):
    """serializer for favorites"""
    class Meta:
        model = Favorite
        depth = 1
        fields = ('id', 'trip_id', 'traveler_id')
