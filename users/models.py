from django.db import models
from  django.contrib.auth.models import AbstractUser

GENDER = (
    ("мужской", "мужской"),
    ('жунский', 'жунский')
)
class CustomUser(AbstractUser):
    age = models.IntegerField("возраст", blank= True, null=True)
    gender = models.CharField("пол", choices=GENDER, max_length=200,  blank= True, null=True)
    birthday = models.DateField("день рождение", blank=True, null=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


    def __str__(self):
        return f'{self.username}'
