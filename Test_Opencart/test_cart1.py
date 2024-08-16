#"C:\Users\MR.WICK\PycharmProjects\pythonProject1\chromedriver-win64\chromedriver.exe"

import pytest
class TestClass:
    @pytest.mark.skip
    def test_1(self,setup):
        print("I am,happy")

    def test_2(self,setup):

        print("i, Am good")