from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from api.models.url_data import UrlData
from api.serializers.url_data import UrlDataSerializer

class UrlDataViewSet(viewsets.ModelViewSet):
    queryset = UrlData.objects.all()
    serializer_class = UrlDataSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['url']
    search_fields = ['url']
    ordering_fields = ['id']
