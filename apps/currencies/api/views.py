from calendar import month
from datetime import date, timedelta, datetime
from time import sleep

from dateutil.relativedelta import relativedelta

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from apps.common.utils.currency import DovizKurlari
from apps.currencies.models import Currency, CurrencyAverage, ExchangeRateAverage
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
        last_day_of_month = date.today().replace(day=get_last_day_of_month(date.today().year, date.today().month))

        for single_date in [first_day_of_month + timedelta(days=n) for n in range((last_day_of_month - first_day_of_month).days)]:
            try:
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
            currency = Currency.objects.filter(date__isnull=False).filter(date=single_date).first()
            # currency = self.get_currency_by_date(single_date)
            if currency is not None:
                total_buying += currency.buying
                total_selling += currency.selling
                number_of_days += 1

        print(total_buying, total_selling)
        if number_of_days != 0:
            currency_average = CurrencyAverage.objects.create(
                date=generate_date_string(last_day_of_month.day, last_day_of_month.month, last_day_of_month.year),
                currency="USD",
                buying=total_buying / number_of_days,
                selling=total_selling / number_of_days
            )
            currency_average.save()

        return {"status": "success"}

    def get_currency_by_date(self, date):
        try:
            return Currency.objects.filter(date=date).first()
        except Exception as e:
            return None


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
                #quarterly_buying=total_selling / number_of_days,
                #quarterly_selling=total_selling / number_of_days,
                #annual_buying=total_selling / number_of_days,
                #annual_selling=total_selling / number_of_days,
            )
            currency_average.save()

        return {"status": "success"}

    def get_currency_by_date(self, date):
        try:
            return Currency.objects.filter(date=date).first()
        except Exception as e:
            return None


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


class AddCurrencyByDay(APIView):
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

    def get(self, request, year, month, day, *args, **kwargs):
        """
        Handles the GET request to add a new currency.

        Args:
            request (Request): The request object.
            format (str, optional): The format of the request. Defaults to None.

        Returns:
            Response: A response object with a status indicating the success of the operation.
        """

        result = self.add_currency_dynamically(year, month, day)

        return Response({"status": "success"})

    def add_currency_dynamically(self, year, month, day):
        if month is not None:
            day = date(year, month, day)

        try:
            self.add_currency_for_this_day(day.day, day.month, day.year)
        except Exception as e:
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


def get_last_day_of_month(year, month):
    date = datetime(year, month, 1)
    last_day = date + relativedelta(months=1, days=-1)
    return last_day.day


def get_first_month_of_quarter(year, quarter):
    if quarter == 1:
        return 1
    elif quarter == 2:
        return 4
    elif quarter == 3:
        return 7
    elif quarter == 4:
        return 10
    else:
        pass


def get_mid_month_of_quarter(year, quarter):
    if quarter == 1:
        return 2
    elif quarter == 2:
        return 5
    elif quarter == 3:
        return 8
    elif quarter == 4:
        return 11
    else:
        pass


def get_last_month_of_quarter(year, quarter):
    if quarter == 1:
        return 3
    elif quarter == 2:
        return 6
    elif quarter == 3:
        return 9
    elif quarter == 4:
        return 12
    else:
        pass