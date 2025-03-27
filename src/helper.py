import pandas as pd


def read_csv_file(path):

    data = pd.read_csv(path, encoding='UTF-8', delimiter=';')
    transactions = data.to_dict(orient='records')
    return transactions


def read_excel_file(path):
    data = pd.read_excel(path)
    transactions = data.to_dict(orient='records')
    return transactions