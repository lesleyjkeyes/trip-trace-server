from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from triptraceapi.models import StopCategory, Stop, Category

class StopCategoryView(ViewSet):
    """Stop Category View"""
    def retrieve(self, request, pk):
        try:
            stop_category = StopCategory.objects.get(pk=pk)
            serializer = StopCategorySerializer(stop_category)
            return Response(serializer.data)
        except StopCategory.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        stop_categories = StopCategory.objects.all()
        stop_id = self.request.query_params.get("stop_id", None)
        if stop_id is not None:
            stop_categories = stop_categories.filter(stop_id=stop_id)
        serializer = StopCategorySerializer(stop_categories, many=True)
        return Response(serializer.data)

    def create(self, request):
        stop = Stop.objects.get(id=request.data["stop_id"])
        category = Category.objects.get(id=request.data["category_id"])
        stop_category = StopCategory.objects.create(
            stop=stop,
            category=category
          )
        serializer = StopCategorySerializer(stop_category)
        return Response(serializer.data)
    
    def update(self, request, pk):
        stop_category = StopCategory.objects.get(pk=pk)
        stop_category.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk):
        """Handle DELETE requests for a single post"""
        stop_category = StopCategory.objects.get(pk=pk)
        stop_category.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class StopCategorySerializer(serializers.ModelSerializer):
    """serializer for stop categories"""
    class Meta:
        model = StopCategory
        depth = 1
        fields = ('id', 'category_id', 'stop_id')
