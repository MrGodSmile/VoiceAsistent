import os
from pathlib import Path
from turtle import pd
from docx import Document
import openpyxl


class Create_files():
    @classmethod
    def create_text_file(cls, file_path):
        print("как назовем")
        name = input()
        new_file_path = os.path.join(file_path, name)
        new_path = f"{new_file_path}.txt"
        if os.path.exists(new_path):
            print("Файл уже существует.")
        else:
            with open(new_path, "w") as file:
                print("хотите туда что-то записать?")
                choice = input()
                if choice == "да":
                    print("что именно")
                    text = input()
                    file.write(text)
                elif choice == "нет":
                    print("Ну как хотите")
            print(f"Файл {name} успешно создан")

    @classmethod
    def create_exel_file(cls, file_path):
        print("как назовем")
        name = input()
        new_file_path = os.path.join(file_path, name)
        new_path = f"{new_file_path}.xlsx"
        print(new_path)
        wb = openpyxl.Workbook()
        wb.save(new_path)
        print(f"Файл Excel успешно создан.")


    @classmethod
    def create_word_file(cls, file_path):
        print("как назовем")
        name = input()
        new_file_path = os.path.join(file_path, name)
        new_path = f"{new_file_path}.docx"
        if os.path.exists(new_path):
            print("Файл уже существует.")
        else:
            document = Document()
            document.save(new_path)
            print("хотите туда что-то записать?")
            choice = input()
            if choice == "да":
                print("что именно")
                text = input()
                document.add_paragraph(text)
                document.save(new_path)
            elif choice == "нет":
                print("Ну как хотите")
            print(f"Файл {name} успешно создан")


def create_folder():
    # Получаем путь к рабочему столу
    desktop_path = (r"C:\Users\mrgod\OneDrive\Рабочий стол")
    print("Как назовем папку?")
    name = input()
    # Создаем полный путь к новой папке на рабочем столе
    new_folder_path = os.path.join(desktop_path, name)

    # Проверяем, существует ли папка уже
    if os.path.exists(new_folder_path):
        print("Папка уже существует.")
    else:
        # Создаем папку на рабочем столе
        os.mkdir(new_folder_path)
        print("Папка успешно создана.")

def create_file():
    desktop_path = (r"C:\Users\mrgod\OneDrive\Рабочий стол")
    print("В какой папке создать файл")
    folder = input()

    # Создаем полный путь к новой папке на рабочем столе
    new_folder_path = os.path.join(desktop_path, folder)

    # Проверяем, существует ли папка уже
    if os.path.exists(new_folder_path):
        print("Какого типа файл вы хотите создать?\n1.Текстовый\n2.Эксель\n3.Ворд")
        name = input()
        if name == "текстовый":
            cf = Create_files()
            cf.create_text_file(new_folder_path)
        elif name == "эксель":
            cf = Create_files()
            cf.create_exel_file(new_folder_path)
        elif name == "ворд":
            cf = Create_files()
            cf.create_word_file(new_folder_path)

    else:
        print("Такой папки нету, Вначале создайте ее с помощью голосовой команды")

create_file()