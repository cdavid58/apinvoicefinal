from django.contrib import admin
from .models import *

class Invoice_POSAdmin(admin.ModelAdmin):
    list_display = ['consecutive','code', 'description','quanty','price','date',]
    search_fields = ['description','code',]

admin.site.register(Invoice_POS,Invoice_POSAdmin)
admin.site.register(Wallet_POS)
