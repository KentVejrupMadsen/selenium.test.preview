from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


import time


class BrowserFrame:
    __browser = None
    __options = None
    __links = []

    def __init__(self):
        self.setup_chrome()
        pass

    def setup_chrome(self):
        self.__options = webdriver.ChromeOptions()
        self.__options.add_argument("user-data-dir=D:\\Workspace\\selenium.test.preview\\user-data")
        self.__browser = webdriver.Chrome( options=self.__options)

    def load(self, url):
        self.__browser.get(url)

    def implicit_wait(self, seconds):
        time.sleep(seconds)

    def add_link(self, uri):
        self.__links.append(uri)

    def execute(self):
        iteration = 0

        for link in self.__links:
            iteration = iteration + 1

            self.load(link)

            self.implicit_wait(5)

            self.__browser.get_screenshot_as_file('./screenshot/' + str(iteration) + '.png')

            self.implicit_wait(2)

        self.is_done()

    def is_done(self):
        if(self.__browser is not None):
            self.__browser.close()