from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from recording.models import AudioRecord
from result.models import DiagnoseResult

from django.db import IntegrityError

from .authentication import AWSIntegationAuthentication
from .serializers import DiagnoseSerializer


class APIintegrationViewset(ViewSet):
    @action(methods=['post'], detail=False,url_path="set-result", url_name="set-result", authentication_classes=[AWSIntegationAuthentication])
    def set_result(self, request):

        serializer = DiagnoseSerializer(data=request.data)
        if serializer.is_valid():
            filename = serializer.data['filename']
            covid_status = serializer.data['covid_status']
            confidence_rate = serializer.data['confidence_rate']
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
            except IntegrityError as e:
                return Response({
                    "message" : "Diagnosis Result has been set before. Thus override it is not possible",
                    "status" : status.HTTP_409_CONFLICT
                }, status=status.HTTP_409_CONFLICT)

            except AudioRecord.DoesNotExist:
                return Response({
                    "message": "Invalid filename",
                    "status" : status.HTTP_404_NOT_FOUND
                }, status=status.HTTP_404_NOT_FOUND
                )
            except Exception as e:
                return Response(
                    {
                        "message" : "Oops! there was an issue. Please let admin know if the problem still persists",
                        "status" : 500,
                        "error" : str(e)
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        else:
            return Response(
                {
                    "message" : "Invalid data format",
                    "status" : status.HTTP_422_UNPROCESSABLE_ENTITY,
                    "errors" : serializer.errors
                },
                status=status.HTTP_422_UNPROCESSABLE_ENTITY)
class AuthenticatiorViewset(ViewSet):
    @action(methods=['get'], detail=False,url_path="test", url_name="test_token", authentication_classes=[AWSIntegationAuthentication])
    def test_token(self, request):
        return Response({
            "message" : "Token is Valid. Authentication Succesful",
            "status" : status.HTTP_200_OK,
        },
        status=status.HTTP_200_OK)
