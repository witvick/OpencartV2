#"C:\Users\MR.WICK\PycharmProjects\pythonProject1\chromedriver-win64\chromedriver.exe"

import pytest
class TestClass:
    @pytest.mark.run(order=2)
    def test_1(self,setup):
        print("I am,happy")

    @pytest.mark.run(order=1)
    def test_2(self,setup):

        print("i, Am good")