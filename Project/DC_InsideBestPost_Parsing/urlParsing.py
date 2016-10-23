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
        self.PAGE_NUMBER = 1
        pass

    # 전체적인 함수 실행해주는 함수
    @asyncio.coroutine
    def mainParser(self, galleryUrl):
        listUrl = galleryUrl + '&page=' + str(self.PAGE_NUMBER) + '&exception_mode=recommend'
        behindPageNumber = yield from self.getBehindPageNumber(listUrl)
        htmlSource = yield from self.getHtml(listUrl)
        galleryPostUrl = yield from self.getPostUrl(listUrl)
        print(galleryPostUrl)
        parseData = yield from self.contentParser(htmlSource, galleryPostUrl)
        return parseData

    # 본문 내용 파싱하는 함수
    @asyncio.coroutine
    def contentParser(self, htmlSource, galleryPostUrl):
        try:
            soup = BeautifulSoup(htmlSource, 'lxml')
            postNumberList = yield from self.getPostNumber(soup)
            postList = list() # 게시글 주소 리스트
            for postNumber in postNumberList:
                postList.append(galleryPostUrl + '&no=' + postNumber)

        except:
            print(traceback.format_exc())
            sys.exit()

    # html 소스 가져오는 함수
    @asyncio.coroutine
    def getHtml(self, url):
        try:
            getHtmlByte = requests.get(url)
            getHtmlString = str(getHtmlByte.text)
            return getHtmlString
        except:
            print(traceback.format_exc())
            sys.exit()

    # 맨 뒷 페이지 번호 파싱
    @asyncio.coroutine
    def getBehindPageNumber(self, listUrl):
        htmlSource = yield from self.getHtml(listUrl)
        soup = BeautifulSoup(htmlSource, 'lxml')
        filterData = re.compile('<span class="arrow_2">')
        filterBehindNumber = re.compile('page=[0-9]+')
        behindPageNumber = self.PAGE_NUMBER
        for b_next in soup.find_all('a', class_='b_next'):
            if filterData.findall(str(b_next)):
                behindPageTag = b_next
                for pageNumber in filterBehindNumber.findall(str(behindPageTag)):
                    behindPageNumber = pageNumber[5:]
        return behindPageNumber



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

    # 개념글 게시글 Url 주소 파싱
    @asyncio.coroutine
    def getPostUrl(self, galleryUrl):
        galleryPostUrl = galleryUrl.replace('lists', 'view')
        return galleryPostUrl