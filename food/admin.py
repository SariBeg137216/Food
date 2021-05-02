from django.contrib import admin
from .models import Item
# Register your models here.

# admin.site.site_header("Food App")
# admin.site.site_title("FoodApplication")
# admin.site.index_title("Food Management")


admin.site.register(Item)

