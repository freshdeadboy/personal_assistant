# personal_assistant/utils.py
import re

def is_valid_phone_number(phone_number):
    # Перевірка правильності формату номера телефону
    phone_pattern = re.compile(r'^\d{3}-\d{4}$')
    return bool(phone_pattern.match(phone_number))

def is_valid_email(email):
    # Перевірка правильності формату email
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return bool(email_pattern.match(email))
