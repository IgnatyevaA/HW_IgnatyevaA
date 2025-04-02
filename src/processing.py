from datetime import datetime

def filter_by_state(operations: list, state: str='EXECUTED') -> list:
    """Фильтрует список словарей по значению ключа 'state'"""
    try:
        return [operation for operation in operations if operation.get('state') == state]
    except ValueError:
        return 'Некорректный ввод данных'


def sort_by_date(operations: list[dict], descending: bool=True) -> list[dict]:
    """Сортирует список словарей по значению ключа 'date'"""
    sorted_values = sorted(
        operations, key=lambda value: value["date"], reverse=descending
    )
    return sorted_values
