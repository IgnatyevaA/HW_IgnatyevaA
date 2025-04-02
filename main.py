import logging

from src.generators import filter_by_currency
from src.new_count import *
from src.processing import filter_by_state, sort_by_date
from src.utils import get_data, done_as_json
from src.widget import *

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logs/main.log', mode='w')  # Перезаписываем файл при каждом запуске
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)





def main():
    user_file = int(input("""Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
"""))

    file_types = {1: "JSON", 2: "CSV", 3: "XLSX"}
    if user_file in file_types:
        print(f"Для обработки выбран {file_types[user_file]}-файл")
        ops = f"data/operations.{file_types[user_file].lower()}"
    else:
        print("Некорректный ввод")
        return
    while True:
        user_state = input("Введите статус для фильтрации (EXECUTED, CANCELED, PENDING): ").upper()
        states = ["EXECUTED", "CANCELED", "PENDING"]
        if user_state in states:
            filtered_ops = done_as_json(filter_by_state(get_data(ops), user_state))
            print(f"Операции отфильтрованы по статусу {user_state}")
            break
        else:
            print(f"Статус операции {user_state} недоступен.")
    logger.debug(f"{filtered_ops} - список json")
    while True:
        user_date = input('Отсортировать операции по дате? Да/Нет ')
        if user_date.lower() == "да":
            sort_date = input('Отсортировать по возрастанию или по убыванию? ')
            if sort_date.lower() == "по возрастанию":
                filtered_ops = sort_by_date(filtered_ops, False)
                break
            elif sort_date.lower() == "по убыванию":
                filtered_ops = sort_by_date(filtered_ops)
                break
            else:
                print("Введите корректный ответ")
        elif user_date.lower() == "нет":
            break
        else:
            print("Введите корректный ответ")
        logger.debug(f"{filtered_ops} - сортировка по времени")
    while True:
        user_cur = input('Выводить только рублевые тразакции? Да/Нет ')
        if user_cur.lower() == "да":
            filtered_ops = filter_by_currency(filtered_ops)
            break
        elif user_cur.lower() == "нет":
            break
        else:
            print("Введите корректный ответ")

        logger.debug(f"{filtered_ops} - сортировка по рублям")
    while True:
        filter_by_word = input("Отфильтровать список транзакций по слову в описании? Да/Нет ")
        if filter_by_word.lower() == "да":
            user_word = input("Введите слово: ")
            filtered_ops = filter_operations_by_string(filtered_ops, user_word)
            break
        elif filter_by_word.lower() == "нет":
            break
        else:
            print("Введите корректный ответ")




    print("\nРаспечатываю итоговый список транзакций...")
    if len(filtered_ops) > 0:
        print(f"Всего банковских операций в выборке: {len(filtered_ops)}")
        for operation in filtered_ops:
            print(f"{get_date(operation['date'])} {operation.get('description', '')}")
            from_acc = operation.get("from")
            to_acc = operation.get("to")
            if from_acc:
                print(f"{mask_account_card(from_acc)} -> {mask_account_card(to_acc)}")
            else:
                print(f"{mask_account_card(to_acc)}")
            amount = operation["operationAmount"]["amount"]
            currency = operation["operationAmount"]["currency"]["name"]
            print(f"Сумма: {amount} {currency}\n")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

if __name__ == "__main__":
    main()