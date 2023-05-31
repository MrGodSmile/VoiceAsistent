import os
from pathlib import Path

def passage(file_name, folder):
    for element in os.scandir(folder):
        if element.is_file():
            if element.name == file_name:
                yield folder
                print("нашел")
        else:
            yield from passage(file_name, element.path)
            print("не нашел")

print(*passage('Update.exe',os.chdir(Path.home() / 'AppData\Local\Discord')))