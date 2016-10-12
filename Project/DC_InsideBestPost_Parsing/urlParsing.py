import asyncio
import traceback
import sys
import urllib.request

class UrlParsingClass():
    def __init__(self):
        pass

    @asyncio.coroutine
    def getHtml(self, galleryUrl):
        try:
            return galleryUrl
        except:
            print(traceback.format_exc())
            sys.exit()