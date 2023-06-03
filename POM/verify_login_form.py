from POM_pages.home_page import HomePage
from POM_pages.login_page import LoginPage

def test_login_form(driver, set_username, set_password):
	home = HomePage(driver)

	#go to Login Page
	log = home.nav_to_login_page()

	#check UI
	log.check_page_ui(log.element_selectors, log.elements_numbers)

	#check login with valid login and password
	password = set_password
	username = set_username
	log.login(username, password)
	assert log.verify_success_message() == 'Welcome to the Secure Area. When you are done click logout below.'
	log.logout()

	#check login with invalid login and password
	invalid_username = 'admin'
	invalid_password = 'admin!'
	log.login(invalid_username, invalid_password)
	log.check_error_banner()
	log.close_error_banner()

	#check login without password
	set_password = None
	log.login(username, set_password)
	log.check_error_banner()
	log.close_error_banner()

	#check login without username
	set_username = None
	log.login(set_username, password)
	log.check_error_banner()
	log.close_error_banner()
