from django.contrib import admin
from apps.financials.models import FinancialTable, Mizan


@admin.register(FinancialTable)
class FinancialTableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in FinancialTable._meta.fields]
    list_display_links = ["account_code", "converter_type"]
    search_fields = ["account_code", "converter_type"]
    list_filter = ["created_at"]

    class Meta:
        model = FinancialTable


@admin.register(Mizan)
class MizanAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Mizan._meta.fields]
    list_display_links = ["account_code", "account_name"]
    search_fields = ["account_code", "account_name"]
    list_filter = ["created_at"]

    class Meta:
        model = Mizan
