from datetime import date, timedelta, datetime
from dateutil.relativedelta import relativedelta


def generate_date_string(day, month, year):
    return f"{year}-{month}-{day}"


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


def get_last_day_of_year(year):
    last_day = datetime(year, 12, 31)
    return last_day
