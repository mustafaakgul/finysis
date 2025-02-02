import numpy as np
import pandas as pd
import xlrd
import os

from decimal import Decimal
from django.shortcuts import render

from apps.common.utils.validation import validate_mizan
from apps.financials.models import Mizan, MizanByDate


def index(request):
    return render(request, "pages/dashboard/finance-performance.html")


def single_data(request):
    data = Mizan.objects.filter(date='28.02.2022')
    return render(request, "pages/dashboard/single-data.html", {"data": data})


def cumulative(request):
    mizans = Mizan.objects.all()

    ### Make a query to get the mizans by date
    mizans_by_date_array = []

    # TODO: distinct account_code
    for mizan in mizans:
        mizans_by_date_obj = MizanByDate.objects.create(
        account_code = mizan.account_code,
        account_name = mizan.account_name,
        total_balance_january = get_total_balance_by_account_code_and_date(mizan.account_code, '31.01.2022'),
        total_balance_february = get_total_balance_by_account_code_and_date(mizan.account_code, '28.02.2022'),
        total_balance_march = get_total_balance_by_account_code_and_date(mizan.account_code, '31.03.2022'),
        total_balance_april = get_total_balance_by_account_code_and_date(mizan.account_code, '30.04.2022'),
        total_balance_may = get_total_balance_by_account_code_and_date(mizan.account_code, '31.05.2022'),
        total_balance_june = get_total_balance_by_account_code_and_date(mizan.account_code, '30.06.2022'),
        total_balance_july = get_total_balance_by_account_code_and_date(mizan.account_code, '31.07.2022'),
        total_balance_august = get_total_balance_by_account_code_and_date(mizan.account_code, '31.08.2022'),
        total_balance_september = get_total_balance_by_account_code_and_date(mizan.account_code, '30.09.2022'),
        total_balance_october = get_total_balance_by_account_code_and_date(mizan.account_code, '31.10.2022'),
        total_balance_november = get_total_balance_by_account_code_and_date(mizan.account_code, '30.11.2022'),
        total_balance_december = get_total_balance_by_account_code_and_date(mizan.account_code, '31.12.2022'),
        )
        mizans_by_date_array.append(mizans_by_date_obj)

    return render(request, "pages/dashboard/cumulative-tl.html", {"mizans": mizans_by_date_array})

# Get Mizan by date
def get(request):
    mizans = Mizan.objects.all()

    ### Make a query to get the mizans by date
    mizans_by_date_array = []

    for mizan in mizans:
        mizans_by_date_obj = MizanByDate.objects.create(
        account_code = mizan.account_code,
        account_name = mizan.account_name,
        total_balance_january = get_total_balance_by_account_code_and_date(mizan.account_code, '31.01.2022'),
        total_balance_february = get_total_balance_by_account_code_and_date(mizan.account_code, '28.02.2022'),
        total_balance_march = get_total_balance_by_account_code_and_date(mizan.account_code, '31.03.2022'),
        total_balance_april = get_total_balance_by_account_code_and_date(mizan.account_code, '30.04.2022'),
        total_balance_may = get_total_balance_by_account_code_and_date(mizan.account_code, '31.05.2022'),
        total_balance_june = get_total_balance_by_account_code_and_date(mizan.account_code, '30.06.2022'),
        total_balance_july = get_total_balance_by_account_code_and_date(mizan.account_code, '31.07.2022'),
        total_balance_august = get_total_balance_by_account_code_and_date(mizan.account_code, '31.08.2022'),
        total_balance_september = get_total_balance_by_account_code_and_date(mizan.account_code, '30.09.2022'),
        total_balance_october = get_total_balance_by_account_code_and_date(mizan.account_code, '31.10.2022'),
        total_balance_november = get_total_balance_by_account_code_and_date(mizan.account_code, '30.11.2022'),
        total_balance_december = get_total_balance_by_account_code_and_date(mizan.account_code, '31.12.2022'),
        )
        mizans_by_date_array.append(mizans_by_date_obj)

    return render(request, "docs/common/get.html", {"mizans": mizans_by_date_array})


def get_total_balance_by_account_code_and_date(account_code, date):
    try:
        return Mizan.objects.get(account_code=account_code, date=date).total_balance
    except Mizan.DoesNotExist:
        return 0


def insert_data(request):
    date_as_string = '31.12.2022'
    data = pd.read_excel('/Users/mustafaakgul/Documents/GitHub/finysis/test.xlsx', sheet_name=date_as_string)
    data.replace(np.nan, 0, inplace=True) # Not None, but 0
    new = data
    for  row in data.itertuples():
        mizan = Mizan.objects.create(
            account_code=str(row[1]),
            account_name=str(row[2]),
            account_currency_type=str(row[3]),
            debit=Decimal(row[4]),
            credit=Decimal(row[5]),
            debit_balance=Decimal(row[6]),
            credit_balance=Decimal(row[7]),
            date = date_as_string
        )

        mizan.total_balance = mizan.debit_balance - mizan.credit_balance
        mizan.save()

    return render(request, "docs/common/add.html")


def insert_by_month(request, date):
    date_as_string = date
    file_path = '/Users/mustafaakgul/Documents/GitHub/finysis/test.xlsx'
    data = pd.read_excel('/Users/mustafaakgul/Documents/GitHub/finysis/test.xlsx', sheet_name=date_as_string)
    data.replace(np.nan, 0, inplace=True)  # Not None, but 0

    result = validate_mizan(data, file_path)
    if result != True:
        return render(request, "docs/common/error.html", {"errors": result})

    for row in data.itertuples():
        mizan = Mizan.objects.create(
            account_code=str(row[1]),
            account_name=str(row[2]),
            account_currency_type=str(row[3]),
            debit=Decimal(row[4]),
            credit=Decimal(row[5]),
            debit_balance=Decimal(row[6]),
            credit_balance=Decimal(row[7]),
            date = date_as_string
        )

        mizan.total_balance = mizan.debit_balance - mizan.credit_balance
        mizan.save()

        # Inserting Cumulative Data
        try:
            mizan_by_date = MizanByDate.objects.get(account_code=mizan.account_code)
            mizan_by_date = insert_by_month(mizan_by_date, mizan)
            mizan_by_date.save()
        except MizanByDate.DoesNotExist:
            mizan_by_date = MizanByDate.objects.create(
                account_code=mizan.account_code,
                account_name=mizan.account_name
            )
            mizan_by_date = insert_by_month(mizan_by_date, mizan)
            mizan_by_date.save()

    return render(request, "docs/common/add.html")


def insert_by_month(mizan_by_date, mizan):
    date_as_string = mizan.date
    if date_as_string == '31.01.2022':
        mizan_by_date.total_balance_january = mizan.total_balance
    elif date_as_string == '28.02.2022':
        mizan_by_date.total_balance_february = mizan.total_balance
    elif date_as_string == '31.03.2022':
        mizan_by_date.total_balance_march = mizan.total_balance
    elif date_as_string == '30.04.2022':
        mizan_by_date.total_balance_april = mizan.total_balance
    elif date_as_string == '31.05.2022':
        mizan_by_date.total_balance_may = mizan.total_balance
    elif date_as_string == '30.06.2022':
        mizan_by_date.total_balance_june = mizan.total_balance
    elif date_as_string == '31.07.2022':
        mizan_by_date.total_balance_july = mizan.total_balance
    elif date_as_string == '31.08.2022':
        mizan_by_date.total_balance_august = mizan.total_balance
    elif date_as_string == '30.09.2022':
        mizan_by_date.total_balance_september = mizan.total_balance
    elif date_as_string == '31.10.2022':
        mizan_by_date.total_balance_october = mizan.total_balance
    elif date_as_string == '30.11.2022':
        mizan_by_date.total_balance_november = mizan.total_balance
    elif date_as_string == '31.12.2022':
        mizan_by_date.total_balance_december = mizan.total_balance

    return mizan_by_date