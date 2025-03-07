from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from api.models.domain_data import DomainData
from api.serializers.domain_data import DomainDataSerializer

class DomainDataViewSet(viewsets.ModelViewSet):
    queryset = DomainData.objects.all()
    serializer_class = DomainDataSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['url_id']
    search_fields = ['domain', 'title']
    ordering_fields = ['created_at']
