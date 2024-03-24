from multiprocessing import Process
from loop import Loop
import os
import sys

loop = Loop()

def clearScreen():
    if os.name == "darwin" or os.name == "posix":
        os.system('clear')

if __name__ == '__main__':
    clearScreen()
    print('''
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@ █████               █████ █████            @
@░░███               ░░███ ░░███             @
@ ░███ █████  ██████  ░███  ░███ █ ████████  @
@ ░███░░███  ███░░███ ░███████████░░███░░███ @
@ ░██████░  ░███ ░███ ░░░░░░░███░█ ░███ ░███ @
@ ░███░░███ ░███ ░███       ░███░  ░███ ░███ @
@ ████ █████░░██████        █████  ████ █████@
@░░░░ ░░░░░  ░░░░░░        ░░░░░  ░░░░ ░░░░░ @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
''')
    try:
        print("Welcome to Koan, a tool to help you focus on your work")
        print("Koan will help you focus on your work by analyzing your desktop screenshots\n")
        print("Enter q or quit to exit and press enter\n")
        try:
            prompt = input('Enter what you wish to work on\nA physics research paper, perhaps: ')
        except Exception as e:
            print(str(e))
            pass
        if prompt == 'q' or prompt == 'quit':
            loop.end_loop()
            sys.exit(0)
        loop.new_loop(prompt)
        while True:
                p = input("Enter q or quit to exit and press enter\n")
                if p == 'q' or p == 'quit':
                    loop.end_loop()
                    sys.exit(0)
    except Exception as e:
        print(str(e))
        loop.end_loop()
        sys.exit(0)
        pass
