from __future__ import print_function
import os
from os.path import join
import io

class Search_program():
    paths = open("Paths.txt", "a+")
    ready_path = ''

    @classmethod
    def search_program(cls, program):
        for root, dirs, files in os.walk('C:\\'):
            #print ("searching", root)
            if program in files:
                path = "%s" % join(root, program)
                Search_program.paths.write(f"\n{path}")
                break

    @classmethod
    def search_in_txt(cls, program):
        with io.open('Paths.txt', encoding='utf-8') as file:
            for line in file:
                if program in line:
                    print("файл найден")
                    ready_path = line
                    return ready_path
            Search_program.search_program(program)

sp = Search_program()
program = sp.search_in_txt("Discord.exe")
os.startfile(program)