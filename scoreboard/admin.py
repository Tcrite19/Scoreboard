from django.contrib import admin
from .models import Game, User, Library, Wishlist
# Register your models here.

admin.site.register(Game)
admin.site.register(User)
admin.site.register(Library)
admin.site.register(Wishlist)