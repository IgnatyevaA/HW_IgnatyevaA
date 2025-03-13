import os

def log(filename=""):
    """Декоратор для логирования выполнения функций"""
    def my_decorator(func):
        """Декоратор, используемый для регистрации событий"""
        def wrapper(*args, **kwargs):
            """Обертка для функции, добавляющая логирование"""
            try:
                result = func(*args, **kwargs)
                if os.path.isfile(filename):
                    with open(os.path.abspath(filename), "a") as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as e:
                if os.path.isfile(filename):
                    with open(os.path.abspath(filename), "a") as file:
                        file.write(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
        return wrapper
    return my_decorator
