import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class Testparallel:

    def test_chrome(self):
        from selenium.webdriver.chrome.service import Service
        self.ser_obj=Service(r"C:\Users\MR.WICK\PycharmProjects\pythonProject1\chromedriver-win64\chromedriver.exe")
        self.driver=webdriver.Chrome(service=self.ser_obj)
        self.driver.get("https://developer.chrome.com/docs/chromedriver/downloads")

    def test_edge(self):
        from selenium.webdriver.edge.service import Service
        self.ser_obj=Service(r"C:\Users\MR.WICK\PycharmProjects\pythonProject1\edgedriver_win64\msedgedriver.exe")
        self.driver=webdriver.Edge(service=self.ser_obj)
        self.driver.get("https://developer.chrome.com/docs/chromedriver/downloads")

    def test_mozilla(self):
        from selenium.webdriver.firefox.service import Service
        self.ser_obj=Service(r"C:\Users\MR.WICK\PycharmProjects\pythonProject1\geckodriver-v0.34.0-win64\geckodriver.exe")
        self.driver=webdriver.Firefox(service=self.ser_obj)
        self.driver.get("https://developer.chrome.com/docs/chromedriver/downloads")