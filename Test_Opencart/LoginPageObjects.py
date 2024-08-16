from selenium.webdriver import chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class RegisterPage:

#Locators
#register mail
    box_email_xpath="//*[@id='reg_email']"
#login email
    box_log_email_xpath="//*[@id='username']"
#login PAssword
    box_log_password_xpath="//*[@id='password']"
#login button
    button_login_xpath="//*[@id='customer_login']/div[1]/form/p[3]/input[3]"
#Register password
    box_password_xpath="//*[@id='reg_password']"
#register button
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


    def loginEmail(self, email):
        lEmail = self.driver.find_element(By.XPATH, self.box_log_email_xpath)
        lEmail.clear()
        lEmail.send_keys(email)

    def loginPassword(self, password):
        lPass = self.driver.find_element(By.XPATH, self.box_log_password_xpath)
        lPass.clear()
        lPass.send_keys(password)

    def login(self):
        log = self.driver.find_element(By.XPATH, self.button_login_xpath)
        log.click()