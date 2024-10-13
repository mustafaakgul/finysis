from datetime import date, timedelta

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.currencies.models import Currency, CurrencyAverage
from apps.currencies.utils.date_utils import generate_date_string


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
