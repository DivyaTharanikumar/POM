from selenium.webdriver.common.by import By

class BasePageLocators:
	search_box=(By.ID,"twotabsearchtextbox")
	login=(By.ID,"nav-link-accountList")

class LoginPageLocators:
	username_textbox=(By.ID,"ap_email")
	password_textbox=(By.ID,"ap_password")
	signin_button=(By.ID,"signInSubmit")