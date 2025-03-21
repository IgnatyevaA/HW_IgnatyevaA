import logging
from logging import FileHandler

# Настройка логирования
logger = logging.getLogger(__name__)
file_handler = FileHandler('logs/masks.log', mode='w')  # Перезаписываем файл при каждом запуске
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)
def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номера банковской карты"""

    logger.info("Функция get_mask_card_number начала работу")

    card_number_str = str(card_number)
    if card_number_str == '':
        logger.error("Пустой ввод для номера карты")
        return ''
    elif len(card_number_str) == 16 and card_number_str.isdigit():
        card_mask = card_number_str[:6] + "******" + card_number_str[-4:]
        formatted_card_mask = " ".join(card_mask[i:i + 4] for i in range(0, len(card_mask), 4))
        logger.info("Возврат замаскированного номера карты")
        return formatted_card_mask
    else:
        logger.error("Некорректный ввод данных для номера карты")
        return 'Некорректный ввод данных'

def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номера банковского счета"""
    logger.info("Функция get_mask_account начала работу")

    account_number_str = str(account_number)
    if account_number_str == '':
        logger.error("Пустой ввод для номера счета")
        return ''
    elif len(account_number_str) == 20 and account_number_str.isdigit():
        account_mask = "**" + account_number_str[-4:]
        logger.info("Возврат замаскированного номера счета")
        return account_mask
    else:
        logger.error("Некорректный ввод данных для номера счета")
        return 'Некорректный ввод данных'

# Пример использования функций
if __name__ == "__main__":
    card_number = "1234567890123456"
    account_number = "12345678901234567890"

    masked_card = get_mask_card_number(card_number)
    print(f"Замаскированный номер карты: {masked_card}")

    masked_account = get_mask_account(account_number)
    print(f"Замаскированный номер счета: {masked_account}")
