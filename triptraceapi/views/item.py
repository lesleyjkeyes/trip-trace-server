from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from triptraceapi.models import Item, Trip

class ItemView(ViewSet):
    """Item View"""
    def retrieve(self, request, pk):
        try:
            item = Item.objects.get(pk=pk)
            serializer = ItemSerializer(item)
            return Response(serializer.data)
        except Item.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        items = Item.objects.all()
        trip_id = self.request.query_params.get("trip_id", None)
        if trip_id is not None:
            items = items.filter(trip_id=trip_id)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
      
    def create(self, request):
        trip = Trip.objects.get(id=request.data["trip_id"])
        item = Item.objects.create(
            trip=trip,
            title=request.data["title"],
            quantity=request.data["quantity"],
            description=request.data["description"],
          )
        serializer = ItemSerializer(item)
        return Response(serializer.data)
    
    def update(self, request, pk):
        item = Item.objects.get(pk=pk)
        item.title = request.data["title"]
        item.description = request.data["description"]
        item.quantity = request.data["quantity"]
        item.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk):
        """Handle DELETE requests for a single post"""
        item = Item.objects.get(pk=pk)
        item.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ItemSerializer(serializers.ModelSerializer):
    """serializer for items"""
    class Meta:
        model = Item
        depth = 1
        fields = ('id', 'trip', 'quantity', 'description', 'title')
