import pandas as pd


expected_sheet_names = [
'31.01.2022',
'28.02.2022',
'31.03.2022',
'30.04.2022',
'31.05.2022',
'30.06.2022',
'31.07.2022',
'31.08.2022',
'30.09.2022',
'31.10.2022',
'30.11.2022',
'31.12.2022'
]


def validate_mizan(data, file_path):
    if (
        validate_of_sheet_name() and
        validate_of_number_of_columns(data) and
        validate_of_number_of_rows(data) and
        validate_of_data_types() and
        validate_of_name_of_sheet(file_path)
    ):
        return True
    else:
        return False


def validate_of_sheet_name():
    return True


def validate_of_number_of_columns(data):
    df = pd.DataFrame(data)
    number_of_columns = df.shape[1]
    return True if number_of_columns is 9 else False



def validate_of_number_of_rows(data):
    df = pd.DataFrame(data)
    number_of_rows = df.shape[0]
    return True if number_of_rows < 10000 else False


def validate_of_data_types():
    return True


def validate_of_name_of_sheet(file_path):
    sheet_names = pd.ExcelFile(file_path).sheet_names
    return all(elem in sheet_names for elem in expected_sheet_names)
