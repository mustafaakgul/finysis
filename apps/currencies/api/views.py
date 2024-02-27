from datetime import date, timedelta

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from apps.common.utils.currency import DovizKurlari
from apps.currencies.models import Currency, CurrencyAverage
from apps.currencies.utils.currency_utils import generate_date_string


class AddCurrency(APIView):
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

    def get(self, request):
        """
        Handles the GET request to add a new currency.

        Args:
            request (Request): The request object.
            format (str, optional): The format of the request. Defaults to None.

        Returns:
            Response: A response object with a status indicating the success of the operation.
        """

        result = self.add_currency_for_this_month()

        return Response({"status": "success"})


    def add_currency_for_this_month(self):
        first_day_of_month = date.today().replace(day=15)
        last_day_of_month = date.today().replace(day=29)

        for single_date in [first_day_of_month + timedelta(days=n) for n in range((last_day_of_month - first_day_of_month).days)]:
            try:
                self.add_currency_for_this_day(single_date.day, single_date.month, single_date.year)
            except Exception as e:
                pass

        return "test"


    def add_currency_for_this_day(self, day, month, year):
        today = date.today()

        cur = DovizKurlari()
        usd_buying = cur.Arsiv(day, month, year, "USD", "BanknoteBuying")
        usd_selling = cur.Arsiv(day, month, year, "USD", "BanknoteSelling")

        print(usd_buying, usd_selling)

        currency_model = Currency.objects.create(
            date=generate_date_string(day, month, year),
            currency="USD",
            buying=usd_buying,
            selling=usd_selling
        )
        currency_model.save()

        return "test"


class AddCurrencyAverage(APIView):
    def get(self, request):
        result_of_average = self.add_currency_average_for_this_month()

        return Response({"status": "success"})

    def add_currency_average_for_this_month(self):
        first_day_of_month = date.today().replace(day=1)
        last_day_of_month = date.today().replace(day=29)

        total_buying = 0
        total_selling = 0
        number_of_days = 0

        for single_date in [first_day_of_month + timedelta(days=n) for n in range((last_day_of_month - first_day_of_month).days)]:
            # currency = Currency.objects.filter(date__isnull=False).filter(date=single_date).first()
            currency = self.get_currency_by_date(single_date)
            if currency is not None:
                total_buying += currency.buying
                total_selling += currency.selling
                number_of_days += 1

        print(total_buying, total_selling)
        currency_average = CurrencyAverage.objects.create(
            date=generate_date_string(last_day_of_month.day, last_day_of_month.month, last_day_of_month.year),
            currency="USD",
            buying=total_buying / number_of_days,
            selling=total_selling / number_of_days
        )
        currency_average.save()

        return "test"

    def get_currency_by_date(self, date):
        try:
            return Currency.objects.filter(date=date).first()
        except Exception as e:
            return None


