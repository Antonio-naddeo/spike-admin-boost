from django.contrib import admin

from djangoql.admin import DjangoQLSearchMixin

from .models import Account

class AccountAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = ['name', 'state', 'interests', 'birth']
    search_fields = ('name', 'bio')
    list_filter= ('state',)


admin.site.register(Account, AccountAdmin)
