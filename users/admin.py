from django.contrib import admin

from .models import Account

class AccountAdmin(admin.ModelAdmin):
    list_display = ['name', 'state', 'interests', 'birth']
    search_fields = ('name', 'bio')
    list_filter= ('state',)


admin.site.register(Account, AccountAdmin)
