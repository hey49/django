from django.contrib import admin

# Register your models here.
from . import models

# admin.site.register(models.User)

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'password', 'time')