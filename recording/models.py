import time
from typing import Tuple
from django.db import models
import uuid
from accounts.models import Subject
from django.utils import timezone

from deprecated import deprecated

# Create your models here.
import io


def get_date_string():
    tz = timezone.now()
    datestr = timezone.now().strftime(r"%Y-%m-%d")
    return datestr


def upload_to_audio_1(instance, filename):
    return f"recording/{instance.sound_type}/{instance.subject.phone_number}/{get_date_string()}/audio1-mask.wav"


def upload_data_recording(instance: "AudioRecord", filename):
    if not instance.is_prediction_recording:
        return f"recording/contributions/{instance.record_category}/{instance.sound_type}/{instance.subject.phone_number}/{get_date_string()}/audio.wav"
    return f"recording/predictions/{instance.record_category}/{instance.sound_type}/{instance.subject.phone_number}/{get_date_string()}/audio.wav"


@deprecated(reason="Use upload_data_recording instead")
def upload_to_audio_2(instance, filename):
    return f"recording/{instance.sound_type}/{instance.subject.phone_number}/{get_date_string()}/audio2-mask.wav"


def upload_to_audio_3(instance, filename):
    return f"recording/{instance.sound_type}/{instance.subject.phone_number}/{get_date_string()}/audio3-no-mask.wav"


def upload_to_audio_4(instance, filename):
    return f"recording/{instance.sound_type}/{instance.subject.phone_number}/{get_date_string()}/audio4-no-mask.wav"


def upload_to(instance, filename):
    return f"recording/cough/integration/{instance.subject.phone_number}/{get_date_string()}/{str(time.time())}.wav"


class Cough(models.Model):
    """
    [DEPRECATED]
    """

    cough_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    cough_record = models.FileField(upload_to=upload_to)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)


class Breath(models.Model):
    """
    [DEPRECATED]
    """

    breath_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    breath_record = models.FileField(upload_to=upload_to)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)


class AudioRecordSample(models.Model):
    CHOICES = [("cough", "Cough"), ("breath", "Breath")]
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    audio1 = models.FileField(upload_to=upload_to_audio_1, blank=True, null=True)
    audio2 = models.FileField(upload_to=upload_to_audio_2, blank=True, null=True)
    audio3 = models.FileField(upload_to=upload_to_audio_3, blank=True, null=True)
    audio4 = models.FileField(upload_to=upload_to_audio_4, blank=True, null=True)
    upload_time = models.DateTimeField(auto_now_add=True)
    sound_type = models.CharField(max_length=10, choices=CHOICES)  # Cough or Breathing
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    @property
    def get_audio_html_tags(self):
        return f"<div> <audio controls src='{self.audio1.url}'></audio> <audio controls src='{self.audio2.url}'></audio> <audio controls src='{self.audio3.url}'> </audio> </div> "


contribution_choices = [
    ("covid-19", "Covid-19"),
    ("tubercolosis", "Tubercolosis"),
    ("prediction", "Prediction"),
]


class AudioRecord(models.Model):
    CHOICES = [("cough", "Cough"), ("breath", "Breath")]
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    audio = models.FileField(upload_to=upload_data_recording, blank=True, null=True)
    upload_time = models.DateTimeField(auto_now_add=True)
    sound_type = models.CharField(max_length=10, choices=CHOICES)  # Cough or Breathing
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    record_category = models.CharField(
        choices=contribution_choices, max_length=50, default="prediction"
    )

    @property
    def is_prediction_recording(self):
        return self.record_category == "prediction"

    @property
    def get_audio_html_tags(self):
        return f"<div> <audio controls src='{self.audio.url}'></audio></div> "

    # encapsulate business logic for sending data to Swisburne AWS.
    @property
    def aws_file(self) -> Tuple[io.BytesIO, str]:
        """
        Return In-memory representation of the audio file along side with the filename for it
        """
        audio_file = self.audio.file
        audio_file.seek(0)
        buffer = io.BytesIO(audio_file.read())
        buffer.seek(0)

        filename = f"{str(self.pk)}.wav"

        return buffer, filename
