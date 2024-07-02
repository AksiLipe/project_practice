from django.contrib import admin
from .models.User import User
from .models.Rating import Rating
from .models.Symbols import Symbols

admin.site.register(User)
admin.site.register(Rating)
admin.site.register(Symbols)
