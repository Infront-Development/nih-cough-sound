from uuid import uuid4
from django.db import models
import os 
import base64

# Create your models here.
class APIToken(models.Model):
    id =  models.UUIDField(default=uuid4, primary_key=True)
    token = models.CharField(max_length=255, null=False, blank=False)
    owner = models.CharField(max_length=255)

    @classmethod
    def generate_token(cls, owner=""):
        random_bytes = os.urandom(32) # Generate random 16 bytes
        encoded = base64.b64encode(random_bytes)
        decoded = encoded.decode("utf-8")

        return cls(token=decoded, owner=owner)

    @classmethod
    def validate_token(cls, token):
        try:
            token : APIToken = cls.objects.get(token=token)
            return token
        except APIToken.DoesNotExist:
            return None