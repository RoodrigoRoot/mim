from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Banks)
admin.site.register(Countries)
admin.site.register(StatusUser)

admin.site.register(Codes)

@admin.register(Accounts)
class AccountsAdmin(admin.ModelAdmin):
    #list_display = ("user", "code")    
    readonly_fields = ("slug",)

admin.site.register(Benefits)

