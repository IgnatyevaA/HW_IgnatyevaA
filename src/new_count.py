import re
from collections import Counter

def filter_operations_by_string(operations, search_string):
    result = []
    for operation in operations:
        search_field = operation.get("description")
        if re.search(search_string, search_field):
            result.append(operation)
    return result

def count_operations_by_description(operations, descriptions):
    lst = [operation["description"] for operation in operations if operation["description"] in descriptions]
    return Counter(lst)

# Пример использования функций
operations = [
    {
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
    },
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    },
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    }
]

# Фильтрация операций по строке 'MasterCard'
filtered_operations = filter_operations_by_string(operations, 'MasterCard')
print(filtered_operations)

# Подсчет операций по описанию
descriptions = ["Перевод организации"]
operation_counts = count_operations_by_description(operations, descriptions)
print(operation_counts)
