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
        self.response = dict()
        pass

    # 전체적인 함수 실행해주는 함수
    @asyncio.coroutine
    def mainParser(self, galleryUrl):
        listUrl = galleryUrl + '&page=' + str(self.PAGE_NUMBER) + '&exception_mode=recommend'
        behindPageNumber = yield from self.getBehindPageNumber(listUrl)
        #for pageNubmer in range(self.PAGE_NUMBER, int(behindPageNumber)):
        listUrl = galleryUrl + '&page=' + str(1) + '&exception_mode=recommend'
        htmlSource = yield from self.getHtml(listUrl)
        parseData = yield from self.contentParser(htmlSource, listUrl)
        return self.response

    # 본문 내용 파싱하는 함수
    @asyncio.coroutine
    def contentParser(self, htmlSource, listUrl):
        try:
            soup = BeautifulSoup(htmlSource, 'lxml')
            galleryPostUrl = yield from self.getPostUrl(listUrl)
            postNumberList = yield from self.getPostNumber(soup)
            postList = [galleryPostUrl + '&no=' + postNumber for postNumber in postNumberList]
            for postUrl in postList:
                print(postUrl)
                postHtml = yield from self.getHtml(postUrl)
                parsingContentData = yield from self.getContentHtmlInfo(postHtml)

        except:
            print(traceback.format_exc())
            sys.exit()

    # 본문 HTML 소스 중 필요한 부분만 파싱
    @asyncio.coroutine
    def getContentHtmlInfo(self, postHtml):
        soup = BeautifulSoup(postHtml, 'lxml')
        for contentDiv in soup.find_all('dl', class_='wt_subject'):
            print(contentDiv)

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

    # html 소스 json 형식으로 데이터 추출
    @asyncio.coroutine
    def transformJson(self, postHtml):
        print('test')


'''
본문 div = id:dgn_content_de
제목 div = class:wt_subject -> dd태
본문내용 div = app_paragraph="Dc_App_Img_0", app_paragraph="Dc_App_text_0"
'''