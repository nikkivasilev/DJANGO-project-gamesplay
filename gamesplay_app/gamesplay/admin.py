from django.contrib import admin

from gamesplay_app.gamesplay.models import Profile, Game


# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass