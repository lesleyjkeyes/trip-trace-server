from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from triptraceapi.models import Country, Category

class CountryView(ViewSet):
    """Country View"""
    def retrieve(self, request, pk):
        try:
            country = Country.objects.get(pk=pk)
            serializer = CountrySerializer(country)
            return Response(serializer.data)
        except Country.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)
      
class CountrySerializer(serializers.ModelSerializer):
    """serializer for categories"""
    class Meta:
        model = Country
        depth = 1
        fields = ('id', 'alpha2', 'alpha3', 'name')
