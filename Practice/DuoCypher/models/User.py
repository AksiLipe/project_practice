from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(blank=True)
    password = models.CharField(
        max_length=128,
        validators=[
            MinLengthValidator(8),
            RegexValidator(regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$',
                           message='Пароль должен содержать хотя бы одну заглавную букву, одну строчную букву и одну цифру')
        ],
        help_text='Пароль должен быть не менее 8 символов и содержать как минимум одну заглавную букву, одну строчную букву и одну цифру'
    )
