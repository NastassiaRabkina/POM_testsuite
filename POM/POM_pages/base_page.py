from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def wait_for(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_list_of_elements(self, locator):
        return self.driver.find_elements(*locator)  

    def check_element_exists(self, locator):
        elements = self.find_list_of_elements(locator)
        return len(elements)

    def check_page_ui(self, element_selectors, elements_numbers):
        for selector, number in zip(element_selectors, elements_numbers):
            locator = (By.XPATH, selector)
            assert self.check_element_exists(locator) == number

    def wait_until_abscent(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))