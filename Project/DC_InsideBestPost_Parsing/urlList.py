# -*-coding: utf-8 -*-
# This source will be move to database
import sys

class UrlList():
    def __init__(self):
        pass

    def urlList(self, key):
        url = {
            '해외축구': 'http://gall.dcinside.com/board/lists/?id=football_new5',
            '최유정': 'http://gall.dcinside.com/board/lists/?id=youjung'
        }
        if not key in url:
            print('No gallery, select other gallery')
            sys.exit()
        else:
            return url[key]