from django.contrib import admin

from djangoql.admin import DjangoQLSearchMixin
from advanced_filters.admin import AdminAdvancedFiltersMixin

from .models import Account

class InterestsFilter(admin.SimpleListFilter):
    title = 'Interest'
    parameter_name =  'interests'
    template = 'admin_text_filter.html'

    def lookups(self, request, model_admin):
        return ((None, None),)

    def choices(self, changelist):
        query_params = changelist.get_filters_params()
        query_params.pop(self.parameter_name, None)
        all_choice = next(super().choices(changelist))
        all_choice['query_params'] = query_params
        yield all_choice

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            return queryset.filter(interests__contains=value)

class AccountAdmin(AdminAdvancedFiltersMixin, DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = ['name', 'state', 'interests', 'birth']
    search_fields = ('name', 'bio')
    list_filter= ('state', InterestsFilter)
    advanced_filter_fields = ('name', 'state', 'interests', 'birth', 'bio')


admin.site.register(Account, AccountAdmin)
