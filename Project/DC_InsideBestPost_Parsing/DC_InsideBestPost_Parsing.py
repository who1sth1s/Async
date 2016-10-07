import asyncio
import sys

import urlList
import selectOption
from urllib import request
from bs4 import BeautifulSoup

sys.path.append('../')

option = selectOption.SelectOption().selectOption()