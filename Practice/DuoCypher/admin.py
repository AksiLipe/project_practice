from django.contrib import admin
from .models.Rating import Rating
from .models.Symbols import Symbols

admin.site.register(Rating)
admin.site.register(Symbols)
