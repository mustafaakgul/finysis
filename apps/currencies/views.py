from django.shortcuts import render

from apps.common.utils.currency import DovizKurlari
from apps.currencies.models import Currency


def add_this_month(request):
    # cur = DovizKurlari()
    # usd_buying = cur.Arsiv(27,2,2024,"USD","BanknoteBuying")
    # usd_selling = cur.Arsiv(27,2,2024,"USD","BanknoteSelling")
    #
    # print(usd_buying, usd_selling)
    #
    # currency_model = Currency.objects.create(
    #     date=generate_date_string(27, 2, 2024),
    #     currency="USD",
    #     buying=usd_buying,
    #     selling=usd_selling
    # )
    # currency_model.save()

    return render(request, "currencies/add.html")


# def generate_date_string(day, month, year):
#     return f"{year}-{month}-{day}"