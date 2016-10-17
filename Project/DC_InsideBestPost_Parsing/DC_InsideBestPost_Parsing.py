import asyncio
import sys

import selectOption
import urlParsing
from urllib import request
from bs4 import BeautifulSoup

sys.path.append('../')

urlParsingClass = urlParsing.UrlParsingClass()

getOptionResult = selectOption.SelectOption().selectOption()
loop = asyncio.get_event_loop()
value = loop.run_until_complete(urlParsingClass.mainParser(getOptionResult))