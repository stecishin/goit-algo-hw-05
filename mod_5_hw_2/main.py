from typing import Callable
import re

def generator_numbers(text: str):
    # Використовуємо регулярний вираз для пошуку всіх чисел з плаваючою точкою у тексті
    for i in re.findall(r'\b\d+\.\d+\b', text):
        # повертаємо їх як генератор
        yield float(i)

# Викликаємо передану функцію (func) для обробки тексту і отримання чисел
def sum_profit(text: str, func: Callable):
    # Обчислюємо суму цих чисел і повертаємо її
    return sum(func(text))

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")