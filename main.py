from src.new_count import *
from src.widget import *


def main(operations):
    user_file = int(input("""Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
"""))

    file_types = {1: "JSON", 2: "CSV", 3: "XLSX"}
    if user_file in file_types:
        print(f"Для обработки выбран {file_types[user_file]}-файл")
    else:
        print("Некорректный ввод")
        return

    user_state = input("Введите статус для фильтрации (EXECUTED, CANCELED, PENDING): ").upper()
    states = ["EXECUTED", "CANCELED", "PENDING"]
    while user_state not in states:
        user_state = input("Введите корректный статус (EXECUTED, CANCELED, PENDING): ").upper()

    filtered_by_state = [operation for operation in operations if operation["state"] == user_state]
    print(f'Операции отфильтрованы по статусу "{user_state}"')

    sort_by_date = input("Отсортировать операции по дате? (Да/Нет): ").title() == 'Да'
    if sort_by_date:
        sort_order = input("Отсортировать по возрастанию или по убыванию? ").title() == 'Да'
        filtered_by_state.sort(key=lambda x: x["date"], reverse=sort_order)

    filter_ruble_only = input("Выводить только рублевые транзакции? (Да/Нет): ").title() == 'Да'
    if filter_ruble_only:
        filtered_by_state = filter_operations_by_string(filtered_by_state, 'RUB')

    filter_by_word = input("Отфильтровать список транзакций по слову в описании? (Да/Нет): ").title() == 'Да'
    if filter_by_word:
        user_word = input("Введите слово: ")
        filtered_by_state = filter_operations_by_string(filtered_by_state, user_word)

    print("\nРаспечатываю итоговый список транзакций...")

    if filtered_by_state:
        print(f"Всего банковских операций в выборке: {len(filtered_by_state)}\n")
        for operation in filtered_by_state:
            description = operation["description"]
            print(f"{get_date(operation['date'])} {description}")
            if description == "Открытие вклада":
                print(mask_account_card(operation["to"]))
            else:
                print(f"{mask_account_card(operation['from'])} -> {mask_account_card(operation['to'])}")
            print(f"Сумма: {operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}\n")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
