from django.db import models
import uuid
from accounts.models import Subjects
from django.utils import timezone
# Create your models here.

def get_date_string():
    tz = timezone.now()
    datestr = timezone.now().strftime(r"%Y-%m-%d")
    return datestr
def upload_to_audio_1(instance, filename):
    return f"recording/{instance.sound_type}/{instance.subjects.phone_number}/{get_date_string()}/audio1-nomask.wav"
def upload_to_audio_2(instance, filename):
    return f"recording/{instance.sound_type}/{instance.subjects.phone_number}/{get_date_string()}/audio2-nomask.wav"

def upload_to_audio_3(instance, filename):
    return f"recording/{instance.sound_type}/{instance.subjects.phone_number}/{get_date_string()}/audio3-mask.wav"

def upload_to_audio_4(instance, filename):
    return f"recording/{instance.sound_type}/{instance.subjects.phone_number}/{get_date_string()}/audio4-mask.wav"

def upload_to(instance, filename):
    ...

class Cough(models.Model):
    cough_id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False,unique=True)
    cough_record = models.FileField(upload_to=upload_to)
    subjects = models.ForeignKey(Subjects,on_delete=models.CASCADE)

class Breath(models.Model):
    breath_id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False,unique=True)
    breath_record = models.FileField(upload_to=upload_to)
    subjects = models.ForeignKey(Subjects,on_delete=models.CASCADE)



class AudioRecordSample(models.Model):
    CHOICES = [
        ("cough", "Cough"),
        ("breath", "Breath")
        ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False,unique=True)
    audio1 = models.FileField(upload_to=upload_to_audio_1)
    audio2 = models.FileField(upload_to=upload_to_audio_2)
    audio3 = models.FileField(upload_to=upload_to_audio_3)
    audio4 = models.FileField(upload_to=upload_to_audio_4)
    Time = models.DateTimeField(auto_now_add=True)
    sound_type = models.CharField(max_length=10, choices=CHOICES) # Cough or Breathing
    subjects = models.ForeignKey(Subjects,on_delete=models.CASCADE)

    @property
    def get_audio_html_tags(self):
        return f"<div> <audio controls src='{self.audio1.url}'></audio> <audio controls src='{self.audio2.url}'></audio> <audio controls src='{self.audio3.url}'> </audio> </div> "

