from django.db import models
from django.contrib.auth.models import AbstractUser


# from django.core.validators import MinValueValidator, MaxValueValidator

from courses.models import Courses




# Users larning asosiy modeli
class CustomUser(AbstractUser):
    phone = models.IntegerField(null=True)
    region = models.CharField(max_length=50, null=True) # blank=True
    province = models.CharField(max_length=50, null=True)          # tuman
    city = models.CharField(max_length=50, null=True)          # shahar
    profile_picture = models.ImageField(default=f"default_doctor.jpg")
    language = models.CharField(max_length=3, default="uz")
    STAJ_CHOICES = (
            ('student', 'Student'),
            ('ordinat', 'Ordinator'),
            ('magistr', 'Magister'),
            ('doc', 'Doctor')
        )
    staj = models.CharField(max_length=50, choices=STAJ_CHOICES, null=True)

    def __str__(self):
        return f"{self.username}, {self.phone}, {self.region}, {self.province}, {self.city}, {self.profile_picture}, {self.language}"




# # User larning dashboard jadvali
class Dashboard(models.Model):
    buy_date = models.DateField()
    progres = models.IntegerField(default=0)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)





# Ortho Academy data jadvali
class OrthoAcademyData(models.Model):
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)