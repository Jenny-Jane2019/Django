from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    gender = (
        ('male', 'male'),
        ('female', 'female'),
    )
    range = (
        ('<20', '<20'),
        ('20-40', '20-40'),
        ('40-60', '40-60'),
        ('>60', '>60'),
    )
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    speaker_name = models.CharField(max_length=200, null=True)
    speaker_age = models.CharField(max_length=200, choices=range, default='20-40')
    speaker_sex = models.CharField(max_length=200, choices=gender, default='male')
    file = models.FileField(upload_to='audio/', null=True)

    def _str_(self):
        return self.speaker_name

