from django.db import models

from apps.accounts.models import Profile
from apps.common.models import CoreModel
from apps.financials.enums import CURRENCIES


class Mizan(CoreModel):
    # profile = models.ForeignKey(
    #     Profile, on_delete=models.PROTECT, related_name="mizans"
    # )
    account_code = models.CharField(max_length=100, blank=False, null=False)
    account_name = models.CharField(max_length=200, blank=True, null=True)
    account_currency_type = models.CharField(max_length=10, blank=True, null=True) # choices=CURRENCIES,
    debit = models.CharField(max_length=50, default=0.00)
    credit = models.CharField(max_length=50, default=0.00)
    debit_balance = models.CharField(max_length=50, default=0.00)
    credit_balance = models.CharField(max_length=50, default=0.00)
    total_balance = models.CharField(max_length=50, blank=True, null=True)

    # debit = models.DecimalField(max_digits=10, decimal_places=4, default=0.00)
    # credit = models.DecimalField(max_digits=10, decimal_places=4, default=0.00)
    # debit_balance = models.DecimalField(max_digits=10, decimal_places=4, default=0.00)
    # credit_balance = models.DecimalField(max_digits=10, decimal_places=4, default=0.00)
    # total_balance = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)

