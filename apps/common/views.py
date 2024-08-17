import numpy as np
import pandas as pd
import xlrd
import os

from decimal import Decimal
from django.shortcuts import render

from apps.financials.models import Mizan, MizanByDate


def index(request):
    return render(request, "pages/dashboard/finance-performance.html")


def cumu(request):
    mizans = Mizan.objects.all()

    ### Make a query to get the mizans by date
    mizans_by_date = MizanByDate.objects.all()
    mizans_by_date_array = []

    ##total_balance_january_2 = Mizan.objects.get(account_code='1', date='30.04.2022')
    ##total_balance_january_2_total_balance = total_balance_january_2.total_balance
    ##total_balance_january = mizans.objects.filter(account_code='1', date='30.04.2022') ##.total_balance

##TODO: distinct account_code
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
        #print(mizans_by_date_obj)
        mizans_by_date_array.append(mizans_by_date_obj)

    return render(request, "pages/dashboard/cumulative.html", {"mizans": mizans_by_date_array})

# Get Mizan by date
def get(request):
    mizans = Mizan.objects.all()

    ### Make a query to get the mizans by date
    mizans_by_date = MizanByDate.objects.all()
    mizans_by_date_array = []

    ##total_balance_january_2 = Mizan.objects.get(account_code='1', date='30.04.2022')
    ##total_balance_january_2_total_balance = total_balance_january_2.total_balance
    ##total_balance_january = mizans.objects.filter(account_code='1', date='30.04.2022') ##.total_balance

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
        #print(mizans_by_date_obj)
        mizans_by_date_array.append(mizans_by_date_obj)

    return render(request, "docs/common/get.html", {"mizans": mizans_by_date_array})


def get_total_balance_by_account_code_and_date(account_code, date):
    try:
        return Mizan.objects.get(account_code=account_code, date=date).total_balance
    except Mizan.DoesNotExist:
        return 0


"""
'31.01.2022'
'28.02.2022'
'31.03.2022'
'30.04.2022'
'31.05.2022'
'30.06.2022'
'31.07.2022'
'31.08.2022'
'30.09.2022'
'31.10.2022'
'30.11.2022'
'31.12.2022'
"""

def add(request):
    date_as_string = '31.12.2022'
    data = pd.read_excel('/Users/mustafaakgul/Documents/GitHub/finysis/test.xlsx', sheet_name=date_as_string)
    data.replace(np.nan, 0, inplace=True) # Not None, but 0
    new = data
    for  row in data.itertuples():
        #print("index: ", index)
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

        # debit = str(row[4]),
        # credit = str(row[5]),
        # debit_balance = str(row[6]),
        # credit_balance = str(row[7]),

        mizan.total_balance = mizan.debit_balance - mizan.credit_balance

        #mizan.total_balance = Decimal(mizan.debit_balance) - Decimal(mizan.credit_balance)

        mizan.save()

    return render(request, "docs/common/add.html")


def validate_element(element):
    if element == 'nan':
        return None
    return element