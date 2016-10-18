# -*-coding: utf-8-*-

import asyncio
import traceback
import sys
import requests
import datetime
import re

from bs4 import BeautifulSoup

class UrlParsingClass():
    def __init__(self):
        pass

    # 전체적인 함수 실행해주는 함수
    @asyncio.coroutine
    def mainParser(self, galleryUrl):
        (htmlSource, listUrl) = yield from self.getHtml(galleryUrl)
        parseData = yield from self.contentParser(htmlSource, listUrl)
        return parseData

    # html 소스 가져오는 함수
    @asyncio.coroutine
    def getHtml(self, galleryUrl):
        pageNumber = str(1)
        try:
            bestPost = galleryUrl + '&page=' + pageNumber + '&exception_mode=recommend'
            getHtmlByte = requests.get(bestPost)
            getHtmlString = str(getHtmlByte.text)
            return (getHtmlString, bestPost)
        except:
            print(traceback.format_exc())
            sys.exit()

    # 본문 내용 파싱하는 함수
    @asyncio.coroutine
    def contentParser(self, htmlSource, listUrl):
        try:
            soup = BeautifulSoup(htmlSource, 'lxml')
            postNumberList = yield from self.getPostNumber(soup)
            postList = list() # 게시글 주소 리스트
            for postNumber in postNumberList:
                postList.append(listUrl + '&no=' + postNumber)
            print(postList)

        except:
            print(traceback.format_exc())
            sys.exit()

    # 개념글 한 페이지에 있는 모든 게시물 고유 번호 파싱하는 함수 (공지 제외)
    @asyncio.coroutine
    def getPostNumber(self, soup):
        postNumberList = list()
        filterNumber = re.compile('[0-9]+')
        for postNumber in soup.find_all('td', class_='t_notice'):
            if filterNumber.search(postNumber.text) is not None:
                postNumberList.append(postNumber.text)
            else:
                continue
        return postNumberList