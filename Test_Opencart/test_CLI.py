import pytest
import pytest
from selenium.webdriver import chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

class TestCLI:


    def test_CLI(self,setup):
        self.driver=setup
        time.sleep(6)
        self.driver.get("https://www.youtube.com/results?search_query=kuari+pass+trek")
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.close()





