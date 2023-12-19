# tests/test_address_book.py
import unittest
from personal_assistant.address_book import AddressBook

class TestAddressBook(unittest.TestCase):
    def setUp(self):
        self.address_book = AddressBook()

    def test_add_contact(self):
        self.address_book.add_contact("John Doe", "123 Main St", "555-1234", "john@example.com", "1990-01-01")
        self.assertEqual(len(self.address_book.contacts), 1)

    def test_search_contacts(self):
        self.address_book.add_contact("John Doe", "123 Main St", "555-1234", "john@example.com", "1990-01-01")
        self.address_book.add_contact("Jane Smith", "456 Oak St", "555-5678", "jane@example.com", "1995-05-05")

        results = self.address_book.search_contacts("John")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['name'], "John Doe")

    def test_show_birthdays_in_range(self):
        self.address_book.add_contact("John Doe", "123 Main St", "555-1234", "john@example.com", "1990-01-01")
        self.address_book.add_contact("Jane Smith", "456 Oak St", "555-5678", "jane@example.com", "2000-05-05")

        upcoming_birthdays = self.address_book.show_birthdays_in_range(30)
        self.assertEqual(len(upcoming_birthdays), 1)
        self.assertEqual(upcoming_birthdays[0]['name'], "Jane Smith")

    def test_edit_contact(self):
        self.address_book.add_contact("John Doe", "123 Main St", "555-1234", "john@example.com", "1990-01-01")
        self.address_book.edit_contact("John Doe", "John Smith", "789 Elm St", "555-4321", "john.smith@example.com", "1990-01-01")

        edited_contact = [contact for contact in self.address_book.contacts if contact['name'] == "John Smith"]
        self.assertEqual(len(edited_contact), 1)
        self.assertEqual(edited_contact[0]['address'], "789 Elm St")

    def test_delete_contact(self):
        self.address_book.add_contact("John Doe", "123 Main St", "555-1234", "john@example.com", "1990-01-01")
        self.address_book.delete_contact("John Doe")
        self.assertEqual(len(self.address_book.contacts), 0)

if __name__ == '__main__':
    unittest.main()
