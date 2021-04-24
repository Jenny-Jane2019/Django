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
        ('20-30', '20-30'),
        ('30-40', '30-40'),
        ('40-50', '40-50'),
        ('>50', '>50'),
    )
    type = (
        ("Huawei", "Huawei"),
        ("Iphone", "Iphone"),
        ("Samsung", "Samsung"),
        ("Oppo", "Oppo"),
        ("Vivo", "Vivo"),
        ("Millet", "Millet"),
        ("Other", "Other"),
    )
    province = (
        ("Beijing", "Beijing"),
        ("Tianjin", "Tianjin"),
        ("Shanghai", "Shanghai"),
        ("Chongqing", "Chongqing"),
        ("Hebei", "Hebei"),
        ("Henan", "Henan"),
        ("Yunnan", "Yunnan"),
        ("Liaoning", "Liaoning"),
        ("Heilongjiang", "Heilongjiang"),
        ("Hunan", "Hunan"),
        ("Anhui", "Anhui"),
        ("Shandong", "Shandong"),
        ("Xinjiang", "Xinjiang"),
        ("Jiangsu", "Jiangsu"),
        ("Zhejiang", "Zhejiang"),
        ("Jiangxi", "Jiangxi"),
        ("Hubei", "Hubei"),
        ("Guangxi", "Guangxi"),
        ("Gansu", "Gansu"),
        ("Shanxi", "Shanxi"),
        ("Inner Mongolia", "Inner Mongolia"),
        ("Shaanxi", "Shaanxi"),
        ("Jilin", "Jilin"),
        ("Fujian", "Fujian"),
        ("Guizhou", "Guizhou"),
        ("Guangdong", "Guangdong"),
        ("Qinghai", "Qinghai"),
        ("Tibet", "Tibet"),
        ("Sichuan", "Sichuan"),
        ("Ningxia", "Ningxia"),
        ("Hainan", "Hainan"),
        ("Taiwan", "Taiwan"),
        ("Hong Kong", "Hong Kong"),
        ("Macao", "Macao"),
    )
    place = (
        ("living room", "living room"),
        ("dormitory", "dormitory"),
        ("bedroom", "bedroom"),
        ("study", "study"),
        ("Other", "Other"),
    )
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    speaker_name = models.CharField(max_length=200, null=True)
    speaker_age = models.CharField(max_length=200, choices=range, default='20-40')
    speaker_sex = models.CharField(max_length=200, choices=gender, default='male')
    phone_type = models.CharField(max_length=200, choices=type, default='Huawei')
    geography = models.CharField(max_length=200, choices=province, default='Beijing')
    environment = models.CharField(max_length=200, choices=place, default='living room')
    file = models.FileField(null=True)

    def _str_(self):
        return self.speaker_name


class Map(models.Model):
    overlap = models.DecimalField(max_digits=3, decimal_places=1, null=True)

    def _str_(self):
        return self.overlap
