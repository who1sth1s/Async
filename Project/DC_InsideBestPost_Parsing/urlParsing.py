import asyncio
import traceback
import sys
import urllib.request

class UrlParsingClass():
    def __init__(self):
        pass

    @asyncio.coroutine
    def getHtml(self, galleryUrl):
        pageNumber = str(1)
        try:
            bestPost = galleryUrl + '&page=' + pageNumber + '&exception_mode=recommend'
            return bestPost
        except:
            print(traceback.format_exc())
            sys.exit()