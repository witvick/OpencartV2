from selenium.webdriver import chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class RegisterPage:

#Locators
    box_email_xpath="//*[@id='reg_email']"
    box_password_xpath="//*[@id='reg_password']"
    button_register_xpath="//*[@id='customer_login']/div[2]/form/p[3]/input[3]"

#Constructor
    def __init__(self,driver):
        self.driver=driver

#ACTION METHODS

    def setEmail(self,email):
        Email=self.driver.find_element(By.XPATH,self.box_email_xpath)
        Email.clear()
        Email.send_keys(email)

    def setPassword(self, password):
        Password = self.driver.find_element(By.XPATH, self.box_password_xpath)
        Password.clear()
        Password.send_keys(password)

    def register(self):
        Reg = self.driver.find_element(By.XPATH, self.button_register_xpath)
        Reg.click()


