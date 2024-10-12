from django.urls import path
from apps.currencies.api.views import (
    AddCurrency,
    AddCurrencyDynamically,
    AddCurrencyByDay,
    AddCurrencyAverage,
    AddCurrencyPeriodicAverage,
    AddCurrencyPeriodicAverageByQuarter,
)


app_name = "currencies"


urlpatterns = [
    path("add", AddCurrency.as_view(), name="add_currency_api"),
    path("add-dynamically/<int:year>", AddCurrencyDynamically.as_view(), name="add_currency_dynamically_api"),
    path("add-by-day/<int:year>/<int:month>/<int:day>", AddCurrencyByDay.as_view(), name="add_currency_by_day_api"),
    path("add-average", AddCurrencyAverage.as_view(), name="add_currency_average_api"),
    path("add-periodic-average-by-month/<int:year>/<int:month>", AddCurrencyPeriodicAverage.as_view(), name="add_currency_periodic_average_api"),
    path("add-periodic-average-by-quarter/<int:year>/<int:quarter>", AddCurrencyPeriodicAverageByQuarter.as_view(), name="add_currency_periodic_average__by_quarter_api"),
]