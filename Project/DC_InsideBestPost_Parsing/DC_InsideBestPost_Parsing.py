import asyncio
import sys

import urlList
import selectOption
from urllib import request
from bs4 import BeautifulSoup

sys.path.append('../')

selectGalary = input("Input Galary Name : ")
url = urlList.UrlList().urlList(selectGalary)
option = selectOption.SelectOption().selectOption()