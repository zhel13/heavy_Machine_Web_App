from django.contrib import admin

from machinemodel.models import MachineModel


# Register your models here.
@admin.register(MachineModel)
class MachineModelAdmin(admin.ModelAdmin):
    ...