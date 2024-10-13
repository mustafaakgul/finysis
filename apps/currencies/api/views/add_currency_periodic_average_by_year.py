from rest_framework.views import APIView
from rest_framework.response import Response

from apps.currencies.models import ExchangeRateAverage
from apps.currencies.utils.date_utils import get_last_day_of_year


class AddCurrencyPeriodicAverageByYear(APIView):
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

    def get(self, request, year, *args, **kwargs):
        """
        Handles the GET request to add a new currency.

        Args:
            request (Request): The request object.
            format (str, optional): The format of the request. Defaults to None.

        Returns:
            Response: A response object with a status indicating the success of the operation.
        """

        result = self.add_currency_averages(year)

        return Response({"status": "success"})

    def add_currency_averages(self, year):
        currencies = ExchangeRateAverage.objects.filter(date__isnull=False).filter(date__year=year)

        last_date_of_year = get_last_day_of_year(year)
        last_record_of_year = ExchangeRateAverage.objects.filter(date__isnull=False).filter(date=last_date_of_year).filter().first()

        avg_buying = 0
        avg_selling = 0
        total_count = 0

        for currency in currencies:
            avg_buying += currency.monthly_buying
            avg_selling += currency.monthly_selling
            total_count += 1

        last_record_of_year.annual_buying = avg_buying / total_count
        last_record_of_year.annual_selling = avg_selling / total_count
        last_record_of_year.save()

        return {"status": "success"}
