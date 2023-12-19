# tests/test_notebook.py
import unittest
from personal_assistant.notebook import Notebook

class TestNotebook(unittest.TestCase):
    def setUp(self):
        self.notebook = Notebook()

    def test_add_note(self):
        self.notebook.add_note("Meeting Notes", "Discuss project timeline.")
        self.assertEqual(len(self.notebook.notes), 1)

    def test_edit_note(self):
        self.notebook.add_note("Meeting Notes", "Discuss project timeline.")
        self.notebook.edit_note(1, "Updated Meeting Notes", "Reviewed project timeline.")
        edited_note = [note for note in self.notebook.notes if note['title'] == "Updated Meeting Notes"]
        self.assertEqual(len(edited_note), 1)
        self.assertEqual(edited_note[0]['content'], "Reviewed project timeline.")

    def test_delete_note(self):
        self.notebook.add_note("Meeting Notes", "Discuss project timeline.")
        self.notebook.delete_note(1)
        self.assertEqual(len(self.notebook.notes), 0)

if __name__ == '__main__':
    unittest.main()