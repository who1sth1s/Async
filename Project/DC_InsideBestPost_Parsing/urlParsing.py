# -*-coding: utf-8-*-

import asyncio
import traceback
import sys
import urllib.request

class UrlParsingClass():
    def __init__(self):
        pass

    @asyncio.coroutine
    def mainParser(self, galleryUrl):
        htmlSource = yield from self.getHtml(galleryUrl)

    @asyncio.coroutine
    def getHtml(self, galleryUrl):
        pageNumber = str(1)
        try:
            bestPost = galleryUrl + '&page=' + pageNumber + '&exception_mode=recommend'
            getHtmlByte = urllib.request.urlopen(bestPost)
            getHtmlString = str(getHtmlByte.read())
            return getHtmlString
        except:
            print(traceback.format_exc())
            sys.exit()