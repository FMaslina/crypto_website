from django.contrib import admin
from calculator.models import Percent


class PercentAdmin(admin.ModelAdmin):
    list_display = ('percent_type', 'percent_value',)
    search_fields = ('percent_value',)
    list_filter = ('percent_type',)


admin.site.register(Percent, PercentAdmin)
