from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from api.models.raw_data import RawData
from api.serializers.raw_data import RawDataSerializer

class RawDataViewSet(viewsets.ModelViewSet):
    queryset = RawData.objects.all()
    serializer_class = RawDataSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['url_id']
    search_fields = ['raw_data']
    ordering_fields = ['scraped_at']
