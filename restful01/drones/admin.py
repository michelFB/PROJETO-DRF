from django.contrib import admin

from .models import Drone,DroneCategory,Competition, Pilot
class DroneAdmin(admin.ModelAdmin):
    list_display = ["name" ]
    search_fields = ["name"]  
admin.site.register(Drone, DroneAdmin)
class DroneCategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
admin.site.register(DroneCategory, DroneCategoryAdmin)
class PilotAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
admin.site.register(Pilot, PilotAdmin)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ["distance_in_feet"]
    search_fields = ["distance_in_feet"]
admin.site.register(Competition, CompetitionAdmin)
