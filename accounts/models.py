from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid

USER_ROLE = (
    ('Staff', 'Staff'),
)

# Create your models here.
class MyAccountManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self, email, first_name, last_name, password, role, phone_number):
        if not email:
            raise ValueError("Users must have email address")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            role=role,
            phone_number=phone_number,
            password=password
        )

        if (role == 'Administrator'):
            user.is_staff = True
            user.is_superuser = True
        else:
            user.is_staff = False
            user.is_superuser = False

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password, role, phone_number):

        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
            last_name=last_name,
            role=role,
            phone_number=phone_number,
        )

        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user

class Account(AbstractBaseUser, PermissionsMixin):
    account_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=60, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20,null=True)
    role = models.CharField(choices=USER_ROLE, max_length=20)
    profile_pic = models.ImageField(default="undraw_profile.svg",null=True, blank=True,upload_to = "img")
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'role','phone_number']

    objects = MyAccountManager()


class Subjects(models.Model):
    subjects_id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False,unique=True)
    subjects_login= models.CharField(max_length=50, unique=True,null=True)
    subjects_phone_number = models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.subjects_login