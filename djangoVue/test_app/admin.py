from django.contrib import admin
from test_app import models

# Register your models here.


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name',)
