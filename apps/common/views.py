import pandas as pd
import xlrd
import os

from django.shortcuts import render

from apps.financials.models import Mizan


def add(request):
    data = pd.read_excel('/Users/mustafaakgul/Documents/GitHub/finysis/test.xlsx', sheet_name='31.01.2022')

    for  row in data.itertuples():
        #print(row.loc[1])
        #print(row[1])
        #print("index: ", index)
        mizan = Mizan.objects.create(
            account_code=str(row[0]),
            account_name=str(row[1]),
            account_currency_type=str(row[2]),
            debit=str(row[3]),
            credit=str(row[4]),
            debit_balance=str(row[5]),
            credit_balance=str(row[6]),
        )
        mizan.save()

    return render(request, "common/add.html")
