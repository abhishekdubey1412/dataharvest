from rest_framework import serializers
from api.models.url_data import UrlData

class UrlDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlData
        fields = '__all__'
