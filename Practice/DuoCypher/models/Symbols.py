from django.db import models


class Symbols(models.Model):
    symbol = models.CharField(max_length=1, blank=True)
    answer = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.symbol} - {self.answer}"
