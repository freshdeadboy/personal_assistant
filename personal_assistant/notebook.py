# personal_assistant/notebook.py
import os
import json

class Notebook:
    def __init__(self):
        self.notes = []
        self.file_path = 'C:\\Users\\bened\\Documents\\Homework\\personal_assistant\\.personal_assistant\\json\\notebook.json'
        self.load_data()

    def load_data(self):
        if os.path.exists(self.file_path):
            try:
                print("Loading data from:", self.file_path)
                with open(self.file_path, 'r') as file:
                    self.notes = json.load(file)
            except json.JSONDecodeError:
                print("Failed to decode JSON.")
                self.notes = []
        else:
            print("File does not exist:", self.file_path)
            self.notes = []

    def save_data(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.notes, file, indent=2)

    def add_note(self, title, content):
        note = {'title': title, 'content': content}
        self.notes.append(note)
        self.save_data()

    def list_notes(self):
        return self.notes

    def edit_note(self, index, new_title, new_content):
        # Редагування нотатки за індексом
        if 1 <= index <= len(self.notes):
            note = self.notes[index - 1]
            note['title'] = new_title
            note['content'] = new_content
            self.save_data()

    def delete_note(self, index):
        # Видалення нотатки за індексом
        if 1 <= index <= len(self.notes):
            del self.notes[index - 1]
            self.save_data()

# Перевірка роботи модуля при його виклику напряму
if __name__ == "__main__":
    notebook = Notebook()
    notebook.add_note("Meeting Notes", "Discuss project timeline.")
    notebook.add_note("Shopping List", "Milk, eggs, bread.")
    notebook.list_notes()
    notebook.edit_note(1, "Meeting Minutes", "Reviewed project timeline.")
    notebook.list_notes()
    notebook.delete_note(2)
    notebook.list_notes()
