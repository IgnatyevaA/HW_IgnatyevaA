def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номера банковской карты"""
    card_number_str = str(card_number)
    try:
        if card_number_str == '':
            return ''
        elif len(card_number_str) == 16 and card_number_str.isdigit():
            card_mask = card_number_str[:6] + "******" + card_number_str[-4:]
            formatted_card_mask = " ".join(card_mask[i:i + 4] for i in range(0, len(card_mask), 4))
            return formatted_card_mask
        else:
            return 'Некорректный ввод данных'
    except ValueError:
        return 'Некорректный ввод данных'


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номера банковского счета"""
    account_number_str = str(account_number)
    try:
        if account_number_str == '':
            return  ''
        elif len(account_number_str) == 20 and account_number_str.isdigit():
            account_mask = "**" + account_number_str[-4:]
            return account_mask
        else:
            return 'Некорректный ввод данных'
    except ValueError:
        return 'Некорректный ввод данных'
