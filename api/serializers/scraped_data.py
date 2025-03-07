from rest_framework import serializers
from api.models.scraped_data import ScrapedData

class ScrapedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapedData
        fields = '__all__'
