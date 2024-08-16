import pytest
from selenium.webdriver import chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup(browser):

    if browser=="chrome":
        from selenium.webdriver.chrome.service import Service
        ser_obj = Service(r"C:\Users\MR.WICK\PycharmProjects\pythonProject1\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service=ser_obj)


    elif browser == "edge":
        from selenium.webdriver.edge.service import Service
        ser_obj = Service(r"C:\Users\MR.WICK\PycharmProjects\pythonProject1\edgedriver_win64\msedgedriver.exe")
        driver = webdriver.Edge(service=ser_obj)


    elif browser == "firefox":
        from selenium.webdriver.firefox.service import Service
        ser_obj = Service(r"C:\Users\MR.WICK\PycharmProjects\pythonProject1\geckodriver-v0.34.0-win64\geckodriver.exe")
        driver = webdriver.Firefox(service=ser_obj)


    return driver

def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="my option: type1 or type2")


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


