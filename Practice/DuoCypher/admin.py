from django.contrib import admin
from .models.Rating import Rating
from .models.Symbols import Symbols
from .models.ImageUser import ImageUser

admin.site.register(Rating)
admin.site.register(Symbols)
admin.site.register(ImageUser)
