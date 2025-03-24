import os
import requests
from dotenv import load_dotenv
from unittest.mock import patch

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение API ключа из переменных окружения
api_key = os.getenv("API_KEY")

def get_amount_rub(transaction):
    """Конвертирует сумму транзакции в рубли, если она в другой валюте."""
    # Извлечение кода валюты и суммы из транзакции
    currency_code = transaction['operationAmount']['currency']['code']
    amount = float(transaction['operationAmount']['amount'])

    # Если валюта уже RUB, возвращаем сумму без изменений
    if currency_code == 'RUB':
        return amount

    # Формирование URL для запроса к API
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"

    # Установка заголовков с API ключом
    headers = {"apikey": api_key}

    try:
        # Выполнение API запроса
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Вызовет ошибку для неуспешных запросов

        # Парсинг JSON ответа и возврат конвертированной суммы
        result = response.json()
        return result["result"]
    except requests.RequestException:
        # Обработка ошибки
        print("Error: Unable to convert currency.")
        return None

# Тестовые случаи для get_amount_rub
def test_get_amount_rub():
    # Тест для проверки, что функция корректно возвращает сумму в RUB
    transaction_rub = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }

    assert get_amount_rub(transaction_rub) == 31957.58

@patch("requests.get")
def test_get_amount_rub_usd(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'result': 435.649305}

    transaction_usd = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "5",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }

    assert get_amount_rub(transaction_usd) == 435.649305
    mock_get.assert_called_once()

@patch("requests.get")
def test_get_amount_rub_error(mock_get):
    # Имитация ошибки ответа от API
    mock_get.side_effect = requests.RequestException("Error occurred")

    transaction_usd = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "5",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }

    assert get_amount_rub(transaction_usd) is None
    mock_get.assert_called_once()
