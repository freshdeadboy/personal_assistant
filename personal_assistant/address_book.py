import os
import json
from datetime import datetime, timedelta
import re 

class AddressBook:
    def __init__(self):
        self.contacts = []
        self.file_path = 'C:\\Users\\bened\\Documents\\Homework\\personal_assistant\\.personal_assistant\\json\\address_book.json'
        self.load_data()

    def load_data(self):
        try:
            with open(self.file_path, 'r') as file:
                self.contacts = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # Обробка випадків, коли файл відсутній або порожній
            self.contacts = []

    def save_data(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.contacts, file, indent=2)
            
    def is_valid_phone_number(self, phone):
        # Перевірка правильності формату номера телефону
        pattern = re.compile(r'^\+\d{1,3}-\d{1,14}$')
        return bool(pattern.match(phone))

    def is_valid_input(self, data):
        # Перевірка, чи дані містять лише букви, цифри, пробіли та деякі символи
        return all(char.isalnum() or char.isspace() or char in ('-', '_', '@', '.') for char in data) 

    def add_contact(self):
        while True:
            name = input("Введіть ім'я контакту: ")
            address = input("Введіть адресу контакту: ")
            phone = input("Введіть номер телефону контакту: ")
            email = input("Введіть email контакту: ")
            birthday = input("Введіть день народження контакту (рррр-мм-дд): ")

            if self.is_valid_input(name) and self.is_valid_input(address) and self.is_valid_phone_number(phone) and self.is_valid_email(email) and self.is_valid_input(birthday):
                break
            else:
                print("Некоректно введені дані. Будь ласка, перевірте правильність вводу.")

        contact = {'name': name, 'address': address, 'phone': phone, 'email': email, 'birthday': birthday}
        self.contacts.append(contact)
        self.save_data()

    def list_contacts(self):
        # Виведення списку контактів
        for contact in self.contacts:
            print(contact)

    def search_contacts(self, keyword):
        # Пошук контактів за ім'ям, адресою, номером телефону чи email
        results = [contact for contact in self.contacts if keyword.lower() in str(contact).lower()]
        return results

    def show_birthdays_in_range(self, days):
        # Виведення контактів з днем народження у заданому інтервалі
        current_date = datetime.now()
        target_date = current_date + timedelta(days=days)
        upcoming_birthdays = [contact for contact in self.contacts if self.parse_birthday(contact['birthday']) == target_date.date()]
        return upcoming_birthdays

    def parse_birthday(self, birthday):
        # Допоміжний метод для розбору дня народження
        return datetime.strptime(birthday, '%Y-%m-%d').date()

    def edit_contact(self, old_name, new_name, new_address, new_phone, new_email, new_birthday):
        # Редагування контакту
        for contact in self.contacts:
            if contact['name'] == old_name:
                if not self.is_valid_phone_number(new_phone):
                    print("Некоректний формат нового номера телефону. Введіть у форматі: +код-номер")
                    return
                if not self.is_valid_email(new_email):
                    print("Некоректний формат нової електронної адреси. Введіть у форматі: user@example.com")
                    return

                contact['name'] = new_name
                contact['address'] = new_address
                contact['phone'] = new_phone
                contact['email'] = new_email
                contact['birthday'] = new_birthday
                self.save_data()
                break

    def delete_contact(self, name):
        # Видалення контакту
        self.contacts = [contact for contact in self.contacts if contact['name'] != name]
        self.save_data()

# Перевірка роботи модуля при його виклику напряму
if __name__ == "__main__":
    address_book = AddressBook()
    address_book.add_contact("John Doe", "123 Main St", "555-1234", "john@example.com", "1990-01-01")
    address_book.add_contact("Jane Smith", "456 Oak St", "555-5678", "jane@example.com", "1995-05-05")
    address_book.list_contacts()
    print("Contacts with birthdays in 30 days:")
    print(address_book.show_birthdays_in_range(30))
    address_book.search_contacts("John")
    address_book.edit_contact("John Doe", "John Smith", "789 Elm St", "555-4321", "john.smith@example.com", "1990-01-01")
    address_book.list_contacts()
    address_book.delete_contact("John Smith")
    address_book.list_contacts()     