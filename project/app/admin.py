from django.contrib import admin
from .models import AuthorModel, VideoGameModel

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    fields = ['name', 'last_name', ' birthday', 'country', 'profession']
    list_display = ['name', 'birthday']
    
admin.site.register(AuthorModel, AuthorAdmin)

@admin.register(VideoGameModel)
class VideoGameAdmin(admin.ModelAdmin):
    fields = ['name', 'Release_Date', 'author']
    list_display = ['name']
    