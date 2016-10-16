# -*-coding: utf-8-*-

import asyncio
import traceback
import sys
import requests

from bs4 import BeautifulSoup

class UrlParsingClass():
    def __init__(self):
        pass

    @asyncio.coroutine
    def mainParser(self, galleryUrl):
        htmlSource = yield from self.getHtml(galleryUrl)
        parseData = yield from self.contentParser(htmlSource)
        return parseData

    @asyncio.coroutine
    def getHtml(self, galleryUrl):
        pageNumber = str(1)
        try:
            bestPost = galleryUrl + '&page=' + pageNumber + '&exception_mode=recommend'
            getHtmlByte = requests.get(bestPost)
            getHtmlString = str(getHtmlByte.text)
            return getHtmlString
        except:
            print(traceback.format_exc())
            sys.exit()

    @asyncio.coroutine
    def contentParser(self, htmlSource):
        try:
            soup = BeautifulSoup(htmlSource, 'lxml')
            appendFile = soup.find_all('ul', {'class', 'appending_file'})
            return appendFile

        except:
            print(traceback.format_exc())
            sys.exit()