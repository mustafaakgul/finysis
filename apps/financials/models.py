from django.db import models

#from apps.accounts.models import Profile
from apps.common.models import CoreModel
from apps.financials.enums import CURRENCIES


CONVERTERTYPES = [
    ("average", "average"),
    ("last", "last"),
    ("instant", "instant"),
    ("custom", "custom"),
    ("none", "none")
]


class Mizan(CoreModel):
    # profile = models.ForeignKey(
    #     Profile, on_delete=models.PROTECT, related_name="mizans"
    # )
    date = models.DateField(blank=False, null=False)
    account_code = models.CharField(max_length=100, blank=False, null=False)
    account_name = models.CharField(max_length=200, blank=True, null=True)
    account_currency_type = models.CharField(max_length=10, blank=True, null=True) # choices=CURRENCIES,
    debit = models.DecimalField(max_digits=40, decimal_places=15, default=0)
    credit = models.DecimalField(max_digits=40, decimal_places=15, default=0)
    debit_balance = models.DecimalField(max_digits=40, decimal_places=15, default=0)
    credit_balance = models.DecimalField(max_digits=40, decimal_places=15, default=0)
    total_balance = models.DecimalField(max_digits=40, decimal_places=15, default=0)


class FinancialTable(CoreModel):
    account_code = models.CharField(max_length=100, blank=False, null=False)
    converter_type = models.CharField(max_length=100, choices=CONVERTERTYPES)
