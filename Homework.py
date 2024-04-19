from datetime import datetime, timedelta


def get_days_from_today(date):
    # Перетворення рядка з датою в об'єкт datetime
    target_date = datetime.strptime(date, '%Y-%m-%d').date()

    # Отримання поточної дати
    today = datetime.now().date()

    # Обчислення різниці в днях
    difference = today - target_date

    return difference.days


# Приклад використання функції
date_str = '2021-10-09'
days_difference = get_days_from_today(date_str)
print("Різниця в днях:", days_difference)

# Завдання друге

import random


def get_numbers_ticket(min, max, quantity):
    if (min < 1) or (max > 1000) or (min > max) or (quantity > (max - min + 1)) or (quantity < 1):
        print('invalid comand')
        return []

    numbers = random.sample(range(min, max + 1), quantity)  # вибір унікальних чисел
    return sorted(numbers)


min = int(input('input min numbers 1-999:'))
max = int(input('input max numbers 2-1000:'))
quantity = int(input('input quantity:'))

# results

lottery_numbers = get_numbers_ticket(min, max, quantity)
print("yours lottery numbers:", lottery_numbers)



# Третє завдання
import re

def normalize_phone(phone_numbers):
    sanitized_numbers = []
    for phone in phone_numbers:
        cleaned_number = re.sub(r'[^0-9]', '', phone)
        if not cleaned_number.startswith('+'):
            if cleaned_number.startswith('380'):
                cleaned_number = '+' + cleaned_number
            else:
                cleaned_number = '+38' + cleaned_number
        sanitized_numbers.append(cleaned_number)
    return sanitized_numbers

phone_numbers = [
    "+38(050)123-32-34",
    "0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11"
]

sanitized_numbers = normalize_phone(phone_numbers)
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)



