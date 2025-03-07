from rest_framework import serializers
from api.models.raw_data import RawData

class RawDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawData
        fields = '__all__'
