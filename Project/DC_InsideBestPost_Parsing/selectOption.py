import sys

class SelectOption():
    def __init__(self):
        pass

    def selectOption(self):
        print('-*- Option -*-\n1. Add gallery list\n2. Select gallery\n(Input 1 or 2)')
        inputOption = input("SelectOption : ")
        if inputOption == '1':
            galleryName = input('Input Gallery name : ')
            galleryUrl = input('Input Gallery url : ')
            urlListFile = open('urlList.py', 'a')
        elif inputOption == '2':
            print('select')
        else:
            print('No option, option is only 1 or 2')
            sys.exit()