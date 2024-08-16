#"C:\Users\MR.WICK\PycharmProjects\pythonProject1\chromedriver-win64\chromedriver.exe"

import pytest
class TestClass:

    @pytest.mark.regression
    def test_SignUp(self,setup):
        print("Sign In")
        assert True

    @pytest.mark.sanity
    def test_loginByPhone(self,setup):
        print("Phone Login")
        assert False

    @pytest.mark.sanity
    def test_loginByEmail(self, setup):
        print("Email login")
        assert False

    @pytest.mark.regression
    def test_loginByGoogle(self, setup):
        print("Google Login")
        assert True