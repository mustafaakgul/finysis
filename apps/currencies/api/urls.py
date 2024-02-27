from django.urls import path
from apps.currencies.api.views import AddCurrency, AddCurrencyAverage


app_name = "currencies"


urlpatterns = [
    path("add", AddCurrency.as_view(), name="add_currency_api"),
    path("add-average", AddCurrencyAverage.as_view(), name="add_currency_average_api"),
]