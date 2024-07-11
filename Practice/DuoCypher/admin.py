from django.contrib import admin
from .models.Rating import Rating
from .models.Symbols import Symbols
from .models.ImageUser import ImageUser
from .models.Level import Level
from .models.Progress import Progress

admin.site.register(Rating)
admin.site.register(Symbols)
admin.site.register(ImageUser)
admin.site.register(Level)
admin.site.register(Progress)
