import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

def test_filter_by_currency(transactions):
    test = list(filter_by_currency(transactions, "USD"))
    assert len(test) == 3
    assert all(i["operationAmount"]["currency"]["code"] == "USD" for i in test)

def test_transaction_descriptions(transactions):
    descriptions = list(transaction_descriptions(transactions))
    expected_descriptions = ["Перевод организации", "Перевод со счета на счет", "Перевод со счета на счет",
                             "Перевод с карты на карту", "Перевод организации"]
    assert descriptions == expected_descriptions


@pytest.mark.parametrize("start, end, expected_card_numbers", [
    (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
    (10, 10, ["0000 0000 0000 0010"]),
    (999, 1001, ["0000 0000 0000 0999", "0000 0000 0000 1000", "0000 0000 0000 1001"])])
def test_card_number_generator(start, end, expected_card_numbers):
    card_numbers = list(card_number_generator(start, end))
    assert card_numbers == expected_card_numbers