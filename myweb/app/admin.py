from django.contrib import admin

# Register your models here.
from . import models


# admin.site.register(models.User)
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'password', 'time')


@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(models.Relation)
class RelationAdmin(admin.ModelAdmin):
    list_display = ('c_obj', 'd_obj')