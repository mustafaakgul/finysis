from datetime import date, timedelta
from time import sleep

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.common.utils.currency import DovizKurlari
from apps.currencies.models import Currency
from apps.currencies.utils.date_utils import generate_date_string, get_last_day_of_month


class AddCurrencyDynamically(APIView):
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

        result = self.add_currency_dynamically(year)

        return Response({"status": "success"})

    def add_currency_dynamically(self, year, month=None):
        if month is not None:
            first_day_of_month = date(year, month, 1)
            last_day_of_month = date(year, month, get_last_day_of_month(year, month))
        else:
            first_day_of_month = date(year, 1, 1)
            last_day_of_month = date(year, 12, 31) # TODO: Make this day dynamic

        for single_date in [first_day_of_month + timedelta(days=n) for n in range((last_day_of_month - first_day_of_month).days + 1)]:
            try:
                #print(single_date)
                sleep(1.2)
                self.add_currency_for_this_day(single_date.day, single_date.month, single_date.year)
            except Exception as e:
                #print(e)
                pass

        return {"status": "success"}

    def add_currency_for_this_month(self):
        first_day_of_month = date.today().replace(day=1)
        last_day_of_month = date.today().replace(day=get_last_day_of_month(date.today().year, date.today().month))

        for single_date in [first_day_of_month + timedelta(days=n) for n in range((last_day_of_month - first_day_of_month).days)]:
            try:
                #print(single_date)
                self.add_currency_for_this_day(single_date.day, single_date.month, single_date.year)
            except Exception as e:
                print(e)
                pass

        return {"status": "success"}

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

        return {"status": "success"}
