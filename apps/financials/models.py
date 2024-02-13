from django.db import models

from apps.accounts.models import Profile
from apps.common.models import CoreModel
from apps.financials.enums import CURRENCIES


class Mizan(CoreModel):
    profile = models.ForeignKey(
        Profile, on_delete=models.PROTECT, related_name="links"
    )
    account_code = models.CharField(max_length=100, blank=False, null=False)
    account_name = models.CharField(max_length=200)
    account_currency_type = models.CharField(max_length=10, choices=CURRENCIES)
    debit = models.DecimalField(max_digits=10, decimal_places=4)
    credit = models.DecimalField(max_digits=10, decimal_places=4)
    debit_balance = models.DecimalField(max_digits=10, decimal_places=4)
    credit_balance = models.DecimalField(max_digits=10, decimal_places=4)
    total_balance = models.DecimalField(max_digits=10, decimal_places=4)
