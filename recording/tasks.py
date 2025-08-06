from celery import shared_task
from typing import BinaryIO
from result.models import DiagnoseResult
from django.utils import timezone
import json
import requests

API_ENDPOINT_URL = "http://cough.swincloud.com/api/covid_detect"


@shared_task
def get_audio_prediciction(audio_file: BinaryIO, request_id: str):
    print(request_id)
    with open("hello.txt", "w") as f:
        f.write(request_id)


@shared_task
def predict(phone_number, audio_file, subject):
    print("Analyzing")
    headers = {}
    cough_mp3 = audio_file.open(mode="rb")
    files = {"file": ("cough.wav", cough_mp3, "audio/wav")}
    r = requests.request("POST", API_ENDPOINT_URL, headers=headers, files=files).text
    status = json.loads(r)["message"]
    if status == "":
        status = "Invalid"
    response = {
        "covid_status": status,
        "confidence_rate": 18,
        "phone_number": phone_number,
        "subject": subject,
        "date_created": timezone.now(),
    }
    DiagnoseResult.objects.create(**response)
