# -*-coding: utf-8-*-

import asyncio
import traceback
import sys
import urllib.request

from bs4 import BeautifulSoup

class UrlParsingClass():
    def __init__(self):
        pass

    @asyncio.coroutine
    def mainParser(self, galleryUrl):
        htmlSource = yield from self.getHtml(galleryUrl)
        parseApi = yield from self.contentParser(htmlSource)
        return parseApi

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

    @asyncio.coroutine
    def contentParser(self, htmlSource):
        try:
            return htmlSource

        except:
            print(traceback.format_exc())
            sys.exit()