import asyncio
import traceback
import sys
import urllib.request

class UrlParsing():
    def __init__(self):
        pass

    @asyncio.coroutine
    def getHtml(self, galleryUrl):
        try:
            print('hello!')
        except:
            print(traceback.format_exc())
            sys.exit()