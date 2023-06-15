from selenium.webdriver.support.events import AbstractEventListener
from datetime import datetime
import os

class Listener(AbstractEventListener):
	def on_exception(self, exception, driver):
		filename = os.path.join('/Users/nastassiarabkina/Desktop/py_course/POM/output/screenshots', str(datetime.now())+'.png')
		driver.get_screenshot_as_file(filename)