from os import stat
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from recording.models import AudioRecord
from result.models import DiagnoseResult


class APIintegrationViewset(ViewSet):
    @action(methods=['put'], detail=False, url_name="set-result", authentication_classes=[])
    def set_result(self, request):

        filename = request.data['filename']
        covid_status = request.date['covid_status']
        confidence_rate = request.data['convidence_rate']
        valid = request.data['is_valid']

        uuid = filename.replace(".wav", "")
        try:
            audio_record = AudioRecord.objects.get(uuid)
            diagnose_result = DiagnoseResult.objects.create(
                audio_record = audio_record,
                covid_status = covid_status,
                confidence_rate = confidence_rate
            )

            return Response({
                dict(diagnose_result)
            }, status= status.HTTP_201_CREATED)
        except AudioRecord.DoesNotExist:
            return Response({
                "error": "Invalid filename"
            }, status=status.HTTP_404_NOT_FOUND
            )

                