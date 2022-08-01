from django.contrib import admin
from .models import Buyer
# Register your models here.


class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_at')


admin.site.register(Buyer, BuyerAdmin)
