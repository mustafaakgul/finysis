from django.db import models

#from apps.accounts.models import Profile
from apps.common.models import CoreModel
from apps.financials.enums import CURRENCIES


class Mizan(CoreModel):
    # profile = models.ForeignKey(
    #     Profile, on_delete=models.PROTECT, related_name="mizans"
    # )
    account_code = models.CharField(max_length=100, blank=False, null=False)
    account_name = models.CharField(max_length=200, blank=True, null=True)
    account_currency_type = models.CharField(max_length=10, blank=True, null=True) # choices=CURRENCIES,
    debit = models.DecimalField(max_digits=40, decimal_places=4, default=0)
    credit = models.DecimalField(max_digits=40, decimal_places=4, default=0)
    debit_balance = models.DecimalField(max_digits=40, decimal_places=4, default=0)
    credit_balance = models.DecimalField(max_digits=40, decimal_places=4, default=0)
    total_balance = models.DecimalField(max_digits=40, decimal_places=4, default=0)
    date = models.CharField(max_length=20, blank=True, null=True)


# Make a new class by date and get the mizans by date
class MizanByDate(CoreModel):
    account_code = models.CharField(max_length=100, blank=False, null=False)
    account_name = models.CharField(max_length=200, blank=True, null=True)
    total_balance_january = models.DecimalField(max_digits=40, decimal_places=4, default=0)
    total_balance_february = models.DecimalField(max_digits=40, decimal_places=4, default=0)
    total_balance_march = models.DecimalField(max_digits=40, decimal_places=4, default=0)
    total_balance_april = models.DecimalField(max_digits=40, decimal_places=4, default=0)
    total_balance_may = models.DecimalField(max_digits=40, decimal_places=4, default=0)
    total_balance_june = models.DecimalField(max_digits=40, decimal_places=4, default=0)
    total_balance_july = models.DecimalField(max_digits=40, decimal_places=4, default=0)
    total_balance_august = models.DecimalField(max_digits=40, decimal_places=4, default=0)
    total_balance_september = models.DecimalField(max_digits=40, decimal_places=4, default=0)
    total_balance_october = models.DecimalField(max_digits=40, decimal_places=4, default=0)
    total_balance_november = models.DecimalField(max_digits=40, decimal_places=4, default=0)
    total_balance_december = models.DecimalField(max_digits=40, decimal_places=4, default=0)


