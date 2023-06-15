from POM_pages.home_page import HomePage
from model.user import User

def test_login_form(driver, username, password):
	home = HomePage(driver)

	#go to Login Page
	log = home.nav_to_login_page()

	#check UI
	log.check_page_ui(log.element_selectors, log.elements_numbers)

	#check login with valid login and password
	usr1 = User(username, password)
	log.login(usr1.username, usr1.password)
	assert log.verify_success_message() == 'Welcome to the Secure Area. When you are done click logout below.'
	log.logout()

	#check login with invalid login and password
	usr2 = User('admin', 'admin!')
	log.login(usr2.username, usr2.password)
	log.check_error_banner()
	log.close_error_banner()

	#check login without password
	usr3 = User.create_user_without_password(username)
	log.login(usr3.username, usr3.password)
	log.check_error_banner()
	log.close_error_banner()

	#check login without username
	usr4 = User.create_user_without_username(password)
	log.login(usr4.username, usr4.password)
	log.check_error_banner()
	log.close_error_banner()
