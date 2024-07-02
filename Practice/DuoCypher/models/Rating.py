from django.db import models
from django.contrib.auth.models import User


class Rating(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    rating = models.IntegerField(default=0)
