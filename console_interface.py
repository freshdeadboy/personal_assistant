from personal_assistant import AddressBook, Notebook

class ConsoleInterface:
    def __init__(self):
        self.address_book = AddressBook()
        self.notebook = Notebook()

    def run(self):
        while True:
            print("\nОберіть опцію:")
            print("1. Додати контакт")
            print("2. Показати список контактів")
            print("3. Додати нотатку")
            print("4. Показати список нотаток")
            print("5. Вийти")

            choice = input("Ваш вибір: ")

            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.show_contacts()
            elif choice == "3":
                self.add_note()
            elif choice == "4":
                self.show_notes()
            elif choice == "5":
                print("Дякую за використання! До побачення.")
                break
            else:
                print("Невірний вибір. Спробуйте ще раз.")

    def add_contact(self):
        while True:
            name = input("Введіть ім'я контакту: ")
            address = input("Введіть адресу контакту: ")
            phone = input("Введіть номер телефону контакту: ")
            email = input("Введіть email контакту: ")
            birthday = input("Введіть день народження контакту (рррр-мм-дд): ")

            if all(self.is_not_empty(data) for data in [name, address, phone, email, birthday]):
                if all(self.is_valid_input(data) for data in [name, address, phone, email, birthday]):
                    break
                else:
                    print("Некоректно введені дані. Будь ласка, перевірте правильність вводу.")
            else:
                print("Поле пусте, введіть дані.")

        contact = {'name': name, 'address': address, 'phone': phone, 'email': email, 'birthday': birthday}
        self.contacts.append(contact)
        self.save_data()

    def is_not_empty(self, data):
        # Перевірка, чи дані не є порожніми
        return bool(data)

    def show_contacts(self):
        contacts = self.address_book.list_contacts()
        if contacts:
            for contact in contacts:
                print(contact)
        else:
            print("Немає жодного контакту.")

    def add_note(self):
        title = input("Введіть назву нотатки: ")
        content = input("Введіть текст нотатки: ")

        self.notebook.add_note(title, content)
        print("Нотатка успішно додана.")

    def show_notes(self):
        print("Before loading notes:", self.notebook.list_notes())
        self.notebook.load_data()
        notes = self.notebook.list_notes()
        print("After loading notes:", notes)
        if not notes:
            print("Немає жодної нотатки.")
        else:
            for note in notes:
                print(note)

if __name__ == "__main__":
    console_interface = ConsoleInterface()
    console_interface.run()    