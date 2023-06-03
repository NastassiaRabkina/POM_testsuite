from POM_pages.home_page import HomePage
from POM_pages.login_page import LoginPage

def test_echo_box_displays_message_back(driver):
	home = HomePage(driver)

	#go to Login Page
	log = home.nav_to_login_page()

	#check UI
	log.check_page_ui(log.element_selectors, log.elements_numbers)

	#check login with valid login and password
	valid_creds = ['tomsmith','SuperSecretPassword!']
	log.login(valid_creds)
	assert log.verify_success_message() == 'Welcome to the Secure Area. When you are done click logout below.'
	log.logout()

	#check login with invalid login and password
	invalid_creds = ['admin','admin!']
	log.login(invalid_creds)
	log.check_error_banner()
	log.close_error_banner()

	#check login without password
	log.login_without_password(valid_creds)
	log.check_error_banner()
	log.close_error_banner()

	#check login without username
	log.login_without_username(valid_creds)
	log.check_error_banner()
	log.close_error_banner()
