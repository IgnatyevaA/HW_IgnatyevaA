from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info_account_or_card: str) -> str:
    """Обработка информации о о картах и счетах"""
    try:
        if info_account_or_card == '':
            return ''
        elif "Счет" in info_account_or_card:
            account_split = info_account_or_card.split()
            account_number = account_split[-1]
            masked_number = get_mask_account(account_number)
            return info_account_or_card.replace(account_number, masked_number)
        else:
            card_split = info_account_or_card.split()
            card_number = card_split[-1]
            masked_number = get_mask_card_number(card_number)
            return info_account_or_card.replace(card_number, masked_number)
    except ValueError:
        return 'Некорректный ввод данных'



def get_date(date_str: str) -> str:
    """Функция, которая переделывает входную строку в ДД.ММ.ГГГГ"""
    try:
        if date_str == '':
            return ''
        else:
            date_obj = datetime.fromisoformat(date_str)
            formatted_date = date_obj.strftime("%d.%m.%Y")
            return formatted_date
    except ValueError:
        return 'Некорректный ввод данных'
