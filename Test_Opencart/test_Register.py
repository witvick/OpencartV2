import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from Test_Opencart.LoginPageObjects import RegisterPage


class TestRegister:
    def testRegister(self):
        from selenium.webdriver.chrome.service import Service
        self.ser_obj = Service(r"C:\Users\MR.WICK\PycharmProjects\pythonProject1\chromedriver-win64\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.ser_obj)
        self.driver.get("https://practice.automationtesting.in/my-account/")
        self.driver.maximize_window()


        self.reg=RegisterPage(self.driver)
        self.reg.setEmail("abcdef14@gmail.com")
        self.reg.setPassword("ABCD123KSIL")
        self.reg.register()
        time.sleep(10)
        self.actual_title=self.driver.title
        self.driver.close()
        assert self.actual_title=="My Account – Automation Practice Site"

