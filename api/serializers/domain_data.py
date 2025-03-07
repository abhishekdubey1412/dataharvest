from rest_framework import serializers
from api.models.domain_data import DomainData

class DomainDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DomainData
        fields = '__all__'
