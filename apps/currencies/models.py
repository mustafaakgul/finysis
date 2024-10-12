from django.db import models

from apps.common.models import CoreModel


class Currency(CoreModel):
    date = models.DateField(unique=True)
    currency = models.CharField(max_length=10)
    buying = models.DecimalField(max_digits=40, decimal_places=4, default=0)
    selling = models.DecimalField(max_digits=40, decimal_places=4, default=0)


class CurrencyAverage(CoreModel):
    date = models.DateField(unique_for_month=True)
    currency = models.CharField(max_length=10)
    buying = models.DecimalField(max_digits=40, decimal_places=4, default=0)
    selling = models.DecimalField(max_digits=40, decimal_places=4, default=0)


class ExchangeRateAverage(CoreModel):
    date = models.DateField(unique=True)
    currency = models.CharField(max_length=10)
    monthly_buying = models.DecimalField(max_digits=40, decimal_places=4, default=0)
    monthly_selling = models.DecimalField(max_digits=40, decimal_places=4, default=0)
    quarterly_buying = models.DecimalField(max_digits=40, decimal_places=4, default=0)
    quarterly_selling = models.DecimalField(max_digits=40, decimal_places=4, default=0)
    annual_buying = models.DecimalField(max_digits=40, decimal_places=4, default=0)
    annual_selling = models.DecimalField(max_digits=40, decimal_places=4, default=0)
