import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from Test_Opencart.LoginPageObjects import RegisterPage
class Testlogin:
    def test_login(self,setup):
        # from selenium.webdriver.chrome.service import Service
        # self.ser_obj = Service(r"C:\Users\MR.WICK\PycharmProjects\pythonProject1\chromedriver-win64\chromedriver.exe")
        # self.driver = webdriver.Chrome(service=self.ser_obj)
        self.driver = setup
        time.sleep(6)
        self.driver.get("https://practice.automationtesting.in/my-account/")
        self.driver.maximize_window()

        self.reg = RegisterPage(self.driver)
        self.reg.loginEmail("abcdef14@gmail.com")
        self.reg.loginPassword("ABCD123KSIL")
        self.reg.login()
        time.sleep(10)
        self.actual_title = self.driver.title
        self.driver.close()
        assert self.actual_title == "My Account – Automation Practice Site"