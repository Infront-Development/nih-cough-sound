from rest_framework import serializers


class DiagnoseSerializer(serializers.Serializer):
    covid_status = serializers.CharField(max_length=255)
    confidence_rate = serializers.FloatField()
    filename = serializers.CharField(max_length=255)
