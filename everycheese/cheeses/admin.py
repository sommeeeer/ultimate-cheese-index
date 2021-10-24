from django.contrib import admin
from .models import Cheese
# Register your models here.

class OverrideCheese(admin.ModelAdmin):
    list_max_show_all = 2000


admin.site.register(Cheese, OverrideCheese)
