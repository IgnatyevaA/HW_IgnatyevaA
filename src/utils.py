import csv
import json
import logging

import pandas as pd

# Настройка логирования
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logs/utils.log', mode='w')  # Перезаписываем файл при каждом запуске
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

def get_data(path):
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    operations = []
    if ".json" in path:
        try:
            with open(path, encoding="utf-8") as json_file:
                operations = json.load(json_file)
        except Exception:
            operations = []
    elif ".csv" in path:
        try:
            with open(path, encoding="utf-8") as csv_file:
                reader = csv.DictReader(csv_file, delimiter=";")
                operations = [row for row in reader]
        except Exception:
            operations = []
    elif ".xlsx" in path:
        try:
            df = pd.read_excel(path)
            operations = df.to_dict(orient="records")
        except Exception:
            operations = []

    return operations

def done_as_json(lst: list[dict]) -> list[dict]:
    normalized = []
    for t in lst:
        if "operationAmount" not in t:
            t["operationAmount"] = {
                "amount": t.pop("amount"),
                "currency": {
                    "name": t.pop("currency_name"),
                    "code": t.pop("currency_code"),
                },
            }
        normalized.append(t)
    return normalized