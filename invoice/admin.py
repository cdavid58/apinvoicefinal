from django.contrib import admin
from .models import *

class InventoryAdmin(admin.ModelAdmin):
    list_display = ['code', 'description','quanty','price_1','date',]
    search_fields = ['description','code','consecutive',]

admin.site.register(Invoice_FE)
admin.site.register(Wallet_FE)
