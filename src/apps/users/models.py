from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_TYPE_CHOICES = [
        ("truck_driver", "Truck Driver"),
        ("dispatcher", "Dispatcher"),
    ]

    USER_GENDER_CHOICES = [
        ("erkak", "Erkak"),
        ("ayol", "Ayol"),
    ]

    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    birthday_date = models.DateField(blank=True, null=True)
    gender = models.CharField(
        max_length=20, choices=USER_GENDER_CHOICES, blank=True, null=True
    )
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    user_type = models.CharField(
        max_length=20, choices=USER_TYPE_CHOICES, default="truck_driver"
    )

    def __str__(self):
        return self.username + " | " + self.first_name + " | " + self.last_name


class Profile(models.Model):

    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="user/avatars/%d/", blank=True, null=True)

    def __str__(self):
        return "Profil: " + self.user.username


class Role(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.role.name}"
    


