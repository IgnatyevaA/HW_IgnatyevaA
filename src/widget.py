from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(name_card: Union[str, None]) -> str:
    """Функция для маскировки карты или счета"""
    if not name_card or not isinstance(name_card, str):
        return "Нет данных"

    digits = "".join(ch for ch in name_card if ch.isdigit())

    if "счет" in name_card.lower() or len(digits) == 20:
        return f"Счет {get_mask_account(digits)}"

    letters = "".join(ch for ch in name_card if ch.isalpha() or ch == " ")
    if len(digits) == 16:
        return f"{letters}{get_mask_card_number(digits)}"

    return "Ошибка! Введите корректный номер банковской карты или счета."





def get_date(date: str) -> str:
    """Функция для показа даты в формате ДД.ММ.ГГГГ"""
    if "T" in date:
        year, month, day = date[0:4], date[5:7], date[8:10]
        return f"{day}.{month}.{year}"
    return "Ошибка! Введите корректный формат даты."