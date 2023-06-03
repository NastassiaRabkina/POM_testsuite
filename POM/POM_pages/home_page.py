from selenium.webdriver.common.by import By

from POM_suite.base_page import BasePage
from POM_suite.login_page import LoginPage


class HomePage(BasePage):
    link = (By.XPATH, '(//a)[22]')

    def nav_to_login_page(self):
        self.find(self.link).click()
        return LoginPage(self.driver)
