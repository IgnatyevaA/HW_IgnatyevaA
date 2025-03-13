import os
import requests
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()
api_key = os.getenv("API_KEY")

def get_amount_rub(transaction):
    """Возвращает сумму транзакции в рублях."""
    currency_code = transaction['operationAmount']['currency']['code']
    transaction_amount = float(transaction['operationAmount']['amount'])

    if currency_code == 'RUB':
        return transaction_amount

    conversion_url = (
        f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={transaction_amount}"
    )
    headers = {"apikey": api_key}
    response = requests.get(conversion_url, headers=headers)

    if response.status_code == 200:
        conversion_result = response.json()
        return conversion_result["result"]
    else:
        raise Exception(f"Ошибка: Не удалось получить данные, код статуса {response.status_code}")

def convert_to_rub(transaction):
    """Возвращает сумму транзакции в рублях."""
    return get_amount_rub(transaction)


