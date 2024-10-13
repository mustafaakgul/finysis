from django.urls import path
from apps.currencies.api.views.add_currency import AddCurrency
from apps.currencies.api.views.add_currency_average import AddCurrencyAverage
from apps.currencies.api.views.add_currency_by_day import AddCurrencyByDay
from apps.currencies.api.views.add_currency_dynamically import AddCurrencyDynamically
from apps.currencies.api.views.add_currency_periodic_average import AddCurrencyPeriodicAverage
from apps.currencies.api.views.add_currency_periodic_average_by_quarter import AddCurrencyPeriodicAverageByQuarter
from apps.currencies.api.views.add_currency_periodic_average_by_year import AddCurrencyPeriodicAverageByYear


app_name = "currencies"


urlpatterns = [
    path("add", AddCurrency.as_view(), name="add_currency_api"),
    path("add-dynamically/<int:year>", AddCurrencyDynamically.as_view(), name="add_currency_dynamically_api"),
    path("add-by-day/<int:year>/<int:month>/<int:day>", AddCurrencyByDay.as_view(), name="add_currency_by_day_api"),
    path("add-average", AddCurrencyAverage.as_view(), name="add_currency_average_api"),
    path("add-periodic-average-by-month/<int:year>/<int:month>", AddCurrencyPeriodicAverage.as_view(), name="add_currency_periodic_average_api"),
    path("add-periodic-average-by-quarter/<int:year>/<int:quarter>", AddCurrencyPeriodicAverageByQuarter.as_view(), name="add_currency_periodic_average_by_quarter_api"),
    path("add-periodic-average-by-year/<int:year>", AddCurrencyPeriodicAverageByYear.as_view(), name="add_currency_periodic_average_by_year_api"),
]