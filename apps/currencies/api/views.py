from datetime import date, timedelta

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from apps.common.utils.currency import DovizKurlari
from apps.currencies.models import Currency
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
        first_day_of_month = date.today().replace(day=1)
        last_day_of_month = date.today().replace(day=3)

        for single_date in [first_day_of_month + timedelta(days=n) for n in range((last_day_of_month - first_day_of_month).days)]:
            print(single_date.day, single_date.month, single_date.year)

        return "test"


    def add_currency_for_this_day(self):
        today = date.today()

        cur = DovizKurlari()
        usd_buying = cur.Arsiv(today.day, today.month, today.year, "USD", "BanknoteBuying")
        usd_selling = cur.Arsiv(today.day, today.month, today.year, "USD", "BanknoteSelling")

        print(usd_buying, usd_selling)

        currency_model = Currency.objects.create(
            date=generate_date_string(today.day, today.month, today.year),
            currency="USD",
            buying=usd_buying,
            selling=usd_selling
        )
        currency_model.save()

        return "test"
