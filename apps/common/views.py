import numpy as np
import pandas as pd
import xlrd
import os

from decimal import Decimal
from django.shortcuts import render

from apps.financials.models import Mizan


def add(request):
    data = pd.read_excel('/Users/mustafaakgul/Documents/GitHub/finysis/test.xlsx', sheet_name='31.01.2022')
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
        )

        # debit = str(row[4]),
        # credit = str(row[5]),
        # debit_balance = str(row[6]),
        # credit_balance = str(row[7]),

        mizan.total_balance = mizan.debit_balance - mizan.credit_balance

        #mizan.total_balance = Decimal(mizan.debit_balance) - Decimal(mizan.credit_balance)

        mizan.save()

    return render(request, "common/add.html")


def validate_element(element):
    if element == 'nan':
        return None
    return element