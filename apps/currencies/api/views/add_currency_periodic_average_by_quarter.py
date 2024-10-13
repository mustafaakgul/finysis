from datetime import date

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.currencies.models import ExchangeRateAverage
from apps.currencies.utils.date_utils import (
    get_first_month_of_quarter,
    get_mid_month_of_quarter,
    get_last_month_of_quarter,
    get_last_day_of_month
    )


class AddCurrencyPeriodicAverageByQuarter(APIView):
    """
     This class-based view handles the addition of a new currency.

     It uses token-based authentication and restricts access to admin users only.

     Methods:
         post: Handles the POST request to add a new currency.
     """

    # permission_classes = [permissions.IsAdminUser]

    def post(self, request, format=None):
        """
        Handles the POST request to add a new currency.

        Args:
            request (Request): The request object.
            format (str, optional): The format of the request. Defaults to None.

        Returns:
            Response: A response object with a status indicating the success of the operation.
        """
        return Response({"status": "success"})

    def get(self, request, year, quarter, *args, **kwargs):
        """
        Handles the GET request to add a new currency.

        Args:
            request (Request): The request object.
            format (str, optional): The format of the request. Defaults to None.

        Returns:
            Response: A response object with a status indicating the success of the operation.
        """

        result = self.add_currency_averages(year, quarter)

        return Response({"status": "success"})

    def add_currency_averages(self, year, quarter):
        first_period_of_quarter = date(year, get_first_month_of_quarter(year, quarter), day=get_last_day_of_month(year, get_first_month_of_quarter(year, quarter)))
        mid_period_of_quarter = date(year, get_mid_month_of_quarter(year, quarter), day=get_last_day_of_month(year, get_mid_month_of_quarter(year, quarter)))
        last_period_of_quarter = date(year, get_last_month_of_quarter(year, quarter), day=get_last_day_of_month(year, get_last_month_of_quarter(year, quarter)))

        currency_first = ExchangeRateAverage.objects.filter(date__isnull=False).filter(date=first_period_of_quarter).first()
        currency_mid = ExchangeRateAverage.objects.filter(date__isnull=False).filter(date=mid_period_of_quarter).first()
        currency_last = ExchangeRateAverage.objects.filter(date__isnull=False).filter(date=last_period_of_quarter).first()

        if currency_first is not None and currency_mid is not None and currency_last is not None:
            avg_buying = (currency_first.monthly_buying + currency_mid.monthly_buying + currency_last.monthly_buying) / 3
            avg_selling = (currency_first.monthly_selling + currency_mid.monthly_selling + currency_last.monthly_selling) / 3

        currency_last.quarterly_buying = avg_buying
        currency_last.quarterly_selling = avg_selling
        currency_last.save()

        return {"status": "success"}
