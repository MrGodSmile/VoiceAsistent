from __future__ import print_function
import os
from os.path import join
import io

class Search_program():
    paths = open(r"C:\Users\mrgod\PycharmProjects\VoiceAsistent\tests\Paths.txt", "a+")
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
        with io.open(r'C:\Users\mrgod\PycharmProjects\VoiceAsistent\tests\Paths.txt', encoding='utf-8') as file:
            lines = [line.rstrip() for line in file]
            for line in lines:
                if program in line:
                    print("файл найден")
                    ready_path = line
                    return ready_path
            Search_program.search_program(program)

sp = Search_program()
program = sp.search_in_txt("Discord.exe")

try:
    os.startfile(program)
except:
    print("я искал программу и нашел")