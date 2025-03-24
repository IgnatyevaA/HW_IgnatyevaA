import json
import logging

# Настройка логирования
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logs/utils.log', mode='w')  # Перезаписываем файл при каждом запуске
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

def get_data(path):
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        if data:
            logger.info("Возврат списка словарей с данными о финансовых транзакциях")
            return data
        else:
            logger.error("Пустой файл")
            return []
    except FileNotFoundError:
        logger.error("Файл не найден")
        return []
    except Exception as e:
        logger.error(f"Ошибка при чтении файла: {e}")
        return []

# Пример использования функции
if __name__ == "__main__":
    path = "path/to/your/file.json"
    data = get_data(path)
    print(f"Данные из файла: {data}")
