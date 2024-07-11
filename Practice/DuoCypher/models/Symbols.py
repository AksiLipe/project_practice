from django.db import models


class Symbols(models.Model):
    symbol = models.CharField(max_length=1, blank=True, unique=True)
    answer = models.CharField(max_length=10, blank=True, unique=True)

    def __str__(self):
        return f"{self.symbol} - {self.answer}"
