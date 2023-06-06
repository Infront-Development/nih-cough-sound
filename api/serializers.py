from multiprocessing.sharedctypes import Value
from rest_framework import serializers
import uuid


def uuid_wav_validation(value):
    filename_uuid = value.split(".wav")[0]
    try:
        uuid.UUID(filename_uuid)
    except ValueError:
        raise serializers.ValidationError(detail="filename is not in UUID.wav format")

class DiagnoseSerializer(serializers.Serializer):
    covid_status = serializers.CharField(max_length=255)
    confidence_rate = serializers.FloatField()
    filename = serializers.CharField(max_length=255, validators=[uuid_wav_validation])
