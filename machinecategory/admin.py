from django.contrib import admin

from machinecategory.models import MachineCategory


# Register your models here.
@admin.register(MachineCategory)
class MachineModelAdmin(admin.ModelAdmin):
    list_display = ['category']