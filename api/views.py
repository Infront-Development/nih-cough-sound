from os import stat
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from recording.models import AudioRecord
from result.models import DiagnoseResult


class APIintegrationViewset(ViewSet):
    @action(methods=['put'], detail=False,url_path="set-result", url_name="set-result", authentication_classes=[])
    def set_result(self, request):

        filename = request.data['filename']
        covid_status = request.data['covid_status']
        confidence_rate = request.data['confidence_rate']
        # valid = request.data['is_valid']

        uuid = filename.replace(".wav", "")
        try:
            audio_record = AudioRecord.objects.get(pk=uuid)
            diagnose_result = DiagnoseResult.objects.create(
                audio_record = audio_record,
                covid_status = covid_status,
                confidence_rate = confidence_rate
            )

            return Response({
                "mesasge" : "Diagnosis result set",
                "status" : status.HTTP_200_OK
            }, status= status.HTTP_201_CREATED)
        except AudioRecord.DoesNotExist:
            return Response({
                "message": "Invalid filename",
                "status" : status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND
            )
        except Exception:
            return Response(
                {
                    "message" : "Oops! there was an issue. Please let admin know if the problem still persists",
                    "status" : 500
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
class AuthenticatiorViewset(ViewSet):
    @action(methods=['get'], detail=False,url_path="test", url_name="test_token", authentication_classes=[])
    def test_token(self, request):
        return Response({
            "message" : "Token is Valid. Authentication Succesful",
            "status" : status.HTTP_200_OK
        },
        status=status.HTTP_200_OK)