from datetime import date, timedelta

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.currencies.models import Currency, ExchangeRateAverage
from apps.currencies.utils.date_utils import generate_date_string, get_last_day_of_month


class AddCurrencyPeriodicAverage(APIView):
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

    def get(self, request, year, month, *args, **kwargs):
        """
        Handles the GET request to add a new currency.

        Args:
            request (Request): The request object.
            format (str, optional): The format of the request. Defaults to None.

        Returns:
            Response: A response object with a status indicating the success of the operation.
        """

        result = self.add_currency_averages(year, month)

        return Response({"status": "success"})

    def add_currency_averages(self, year, month):
        first_day_of_month_of_year = date(year, month, 1)
        last_day_of_month_of_year = date(year, month, day=get_last_day_of_month(year, month))

        total_buying = 0
        total_selling = 0
        number_of_days = 0

        for single_date in [first_day_of_month_of_year + timedelta(days=n) for n in
                            range((last_day_of_month_of_year - first_day_of_month_of_year).days)]:
            currency = Currency.objects.filter(date__isnull=False).filter(date=single_date).first()
            if currency is not None:
                total_buying += currency.buying
                total_selling += currency.selling
                number_of_days += 1

        print(total_buying, total_selling)
        if number_of_days != 0:
            currency_average = ExchangeRateAverage.objects.create(
                date=generate_date_string(last_day_of_month_of_year.day, last_day_of_month_of_year.month, last_day_of_month_of_year.year),
                currency="USD",
                monthly_buying=total_buying / number_of_days,
                monthly_selling=total_selling / number_of_days,
                # quarterly_buying=total_selling / number_of_days,
                # quarterly_selling=total_selling / number_of_days,
                # annual_buying=total_selling / number_of_days,
                # annual_selling=total_selling / number_of_days,
            )
            currency_average.save()

        return {"status": "success"}

    def get_currency_by_date(self, date):
        try:
            return Currency.objects.filter(date=date).first()
        except Exception as e:
            return None
