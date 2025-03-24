import json
from unittest.mock import patch, mock_open
from src.utils import get_data

def test_load_data():
    """Тестирует корректность загрузки данных из файла."""
    # Имитация данных, которые должны быть в файле
    mock_data = (
        '[{"id": 441945886, "state": "EXECUTED", '
        '"date": "2019-08-26T10:50:58.294041", '
        '"operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}}, '
        '"description": "Перевод организации", "from": "Maestro 1596837868705199", '
        '"to": "Счет 64686473678894779589"}]'
    )

    # Создание заглушки для функции open, которая будет возвращать наши имитационные данные
    mock_file = mock_open(read_data=mock_data)

    # Использование patch для замены функции open нашей заглушкой
    with patch('builtins.open', mock_file):
        # Вызов функции get_data с путем к файлу
        result = get_data("../data/operations.json")

    # Ожидаемый результат — это наши имитационные данные, преобразованные из JSON
    expected_result = json.loads(mock_data)

    # Проверка, что результат совпадает с ожидаемым
    assert result == expected_result
    # Проверка, что функция open была вызвана один раз
    mock_file.assert_called_once()

def test_load_data_exception():
    """Тестирует поведение функции при отсутствии файла."""
    # Создание заглушки, которая вызывает исключение при попытке открыть файл
    mock_error = mock_open()
    mock_error.side_effect = FileNotFoundError("File not found")

    # Использование patch для замены функции open нашей заглушкой
    with patch("builtins.open", mock_error):
        # Вызов функции get_data с путем к несуществующему файлу
        result = get_data("non_existent.json")

    # Проверка, что результат — пустой список, так как файл не найден
    assert result == []
    # Проверка, что функция open была вызвана один раз
    mock_error.assert_called_once()
