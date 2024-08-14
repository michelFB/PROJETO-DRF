from django.contrib import admin

# Register your models here.
from .models import Toy

class ToyAdmin(admin.ModelAdmin):
     list_display = [
          "name",
          "toy_category",
          "release_date"
     ]
     search_fields = ["name","toy_category"]
     
admin.site.register(Toy,ToyAdmin)