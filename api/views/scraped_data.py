from rest_framework import viewsets, filters
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from api.models.scraped_data import ScrapedData
from api.serializers.scraped_data import ScrapedDataSerializer

class ScrapedDataViewSet(viewsets.ModelViewSet):
    queryset = ScrapedData.objects.all()
    serializer_class = ScrapedDataSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['url_id']
    search_fields = ['name', 'email', 'phone']
    ordering_fields = ['created_at']
