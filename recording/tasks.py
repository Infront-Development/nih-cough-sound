from celery import shared_task
from typing import BinaryIO
@shared_task
def get_audio_prediciction(audio_file : BinaryIO, request_id : str):
    print(request_id)
    with open("hello.txt", "w") as f:
        f.write(request_id)
