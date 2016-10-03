import sys

class SelectOption():
    def __init__(self):
        pass

    def selectOption(self):
        print('-*- Option -*-\n1. Add galary list\n2. Select galary\n(Input 1 or 2)')
        inputOption = input("SelectOption : ")
        if inputOption == '1':
            print('create')
        elif inputOption == '2':
            print('select')
        else:
            print('No option, option is only 1 or 2')
            sys.exit()