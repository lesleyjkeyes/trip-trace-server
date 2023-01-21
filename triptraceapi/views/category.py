from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from triptraceapi.models import StopCategory, Category

class CategoryView(ViewSet):
    """Category View"""
    def retrieve(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        except Category.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
      
    def create(self, request):
        category = Category.objects.create(
            title=request.data["title"]
          )
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    def update(self, request, pk):
        category = Category.objects.get(pk=pk)
        category.title = request.data["title"]
        category.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk):
        """Handle DELETE requests for a single post"""
        category = Category.objects.get(pk=pk)
        category.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class CategorySerializer(serializers.ModelSerializer):
    """serializer for categories"""
    class Meta:
        model = Category
        depth = 1
        fields = ('id', 'title')
