# Banking operations

Наш проект представлен в виде виджета банковских операций клиента.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш_репозиторий.git
   ```
2. Перейдите в директорию проекта:
   ```bash
   cd ваш_проект
   ```
3. Установите необходимые зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## Использование

Примеры использования функций:

```python
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from tests.conftest import transactions

# Пример использования filter_by_state
transactions1 = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 59402872, 'state': 'CANCELLED', 'date': '2018-09-17T21:27:25.241241'}
]
executed_transactions = filter_by_state(transactions1)

# Пример использования sort_by_date
sorted_transactions = sort_by_date(transactions1)

# Пример использования filter_by_currency
usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
 print(next(usd_transactions))

# Пример использования transaction_descriptions
descriptions = transaction_descriptions(transactions)
for _ in range(5):
 print(next(descriptions))

# Пример использования card_number_generator
for card_number in card_number_generator(1, 5):
 print(card_number)
```
Пример использования декоратора:

```
from src.decorators import log

@log(filename='')
def my_function(x, y):
    return x + y

my_function(1, 2)

# >>> my_function ok
```

## Тестирование

В нашем проекте используется тестирование для обеспечения надёжности и корректности работы. Был использован фреймвор pytest.
Все написанные тесты находятся в папке tests, там же можно найти файл со всеми фикстурами в модуле "conftest.py"

```
File	        statements  missing  excluded   coverage
src\__init__.py	    0	        0       0         100%
src\decorators.py   18          2       0         89%
src\generators.py   9           0       0         100%
src\masks.py	    23	        4       0         83%
src\processing.py   11	        2       0         82%
src\widget.py	    28	        3       0         89%
Total	            71	        9       0         87%
```