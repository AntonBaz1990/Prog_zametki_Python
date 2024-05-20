import datetime
import os


class Note:
    def __init__(self, note_id, title, content, timestamp):
        self.note_id = note_id
        self.title = title
        self.content = content
        self.timestamp = timestamp

def create_note(note_list):
    note_id = len(note_list) + 1
    title = input("Введите заголовок заметки: ")
    content = input("Введите текст заметки: ")
    timestamp = datetime.datetime.now()
    note = Note(note_id, title, content, timestamp)
    note_list.append(note)
    save_notes(note_list)
    print("Заметка создана.")

def read_notes(note_list):
    if note_list:
        print("Список заметок:")
        for note in note_list:
            print(f"{note.note_id}. {note.title} - {note.timestamp}")
    else:
        print("У вас нет сохраненных заметок.")

def read_note(note_list, note_id):
    for note in note_list:
        if note.note_id == note_id:
            print(f"Заметка '{note.title}':\n{note.content}\nСоздана: {note.timestamp}")
            return
    print("Заметка не найдена.")

def edit_note(note_list, note_id):
    for note in note_list:
        if note.note_id == note_id:
            new_content = input("Введите новый текст заметки: ")
            note.content = new_content
            note.timestamp = datetime.datetime.now()
            save_notes(note_list)
            print("Заметка отредактирована.")
            return
    print("Заметка не найдена.")

def delete_note(note_list, note_id):
    for note in note_list:
        if note.note_id == note_id:
            note_list.remove(note)
            save_notes(note_list)
            print("Заметка удалена.")
            return
    print("Заметка не найдена.")

def save_notes(note_list):
    with open("notes.txt", "w") as file:
        for note in note_list:
            file.write(f"{note.note_id},{note.title},{note.content},{note.timestamp}\n")

def load_notes():
    if os.path.exists("notes.txt"):
        with open("notes.txt", "r") as file:
            notes = []
            for line in file:
                data = line.strip().split(",")
                note = Note(int(data[0]), data[1], data[2], datetime.datetime.fromisoformat(data[3]))
                notes.append(note)
            return notes
    else:
        return []

# Основной код
notes = load_notes()

while True:
    print("\nМеню:")
    print("1. Показать список заметок")
    print("2. Создать новую заметку")
    print("3. Показать заметку")
    print("4. Редактировать заметку")
    print("5. Удалить заметку")
    print("6. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        read_notes(notes)
    elif choice == "2":
        create_note(notes)
    elif choice == "3":
        note_id = int(input("Введите ID заметки: "))
        read_note(notes, note_id)
    elif choice == "4":
        note_id = int(input("Введите ID заметки для редактирования: "))
        edit_note(notes, note_id)
    elif choice == "5":
        note_id = int(input("Введите ID заметки для удаления: "))
        delete_note(notes, note_id)
    elif choice == "6":
        break
    else:
        print("Некорректный выбор. Пожалуйста, выберите существующий пункт из меню.")
