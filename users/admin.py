from django.contrib import admin

from djangoql.admin import DjangoQLSearchMixin
from advanced_filters.admin import AdminAdvancedFiltersMixin

from .models import Account

class AccountAdmin(AdminAdvancedFiltersMixin, DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = ['name', 'state', 'interests', 'birth']
    search_fields = ('name', 'bio')
    list_filter= ('state',)
    advanced_filter_fields = ('name', 'state', 'interests', 'birth', 'bio')


admin.site.register(Account, AccountAdmin)
