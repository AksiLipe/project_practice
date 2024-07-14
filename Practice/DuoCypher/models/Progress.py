from django.db import models
from django.contrib.auth.models import User
from .Level import Level


class Progress(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    level_id = models.ForeignKey(Level, on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)
