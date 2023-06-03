from POM_pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage(BasePage):

	username_field = (By.CSS_SELECTOR, '#username')
	password_field = (By.CSS_SELECTOR, '#password')
	login_button = (By.CSS_SELECTOR, 'button')
	logout_button =(By.CSS_SELECTOR, 'a[href*=logout]')
	success_massage = (By.TAG_NAME, 'h4')
	error_message = (By.ID, 'flash')
	close_banner_button = (By.CSS_SELECTOR, 'a.close')
	
	def __init__(self, driver):
		super().__init__(driver)
		self.element_selectors = ['//h2', '//h4', '//label', '//input', '//button']
		self.elements_numbers = [1, 1, 2, 2, 1]

	def login(self, creds):
		self.find(self.username_field).send_keys(creds[0])
		self.find(self.password_field).send_keys(creds[1])
		self.find(self.login_button).click()

	def verify_success_message(self):
		text = self.find(self.success_massage).get_attribute('innerText')
		return text

	def logout(self):
		self.find(self.logout_button).click()

	def check_error_banner(self):
		assert self.check_element_exists(self.error_message) == 1

	def close_error_banner(self):
		self.find(self.close_banner_button).click()
		self.wait_until_abscent(self.error_message)	

	def login_without_username(self, creds):
		self.find(self.password_field).send_keys(creds[1])
		self.find(self.login_button).click()

	def login_without_password(self, creds):
		self.find(self.username_field).send_keys(creds[0])
		self.find(self.login_button).click()
