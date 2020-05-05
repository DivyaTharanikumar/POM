from POM.PageElements import *
from selenium.webdriver.common.keys import Keys

class BasePage(object):
	def __init__(self,driver):
		self.driver=driver

	def search_text(self,text):
		bpe=BasePageElements(self.driver)
		tb=bpe.search_text_element()
		tb.send_keys(text)
		tb.send_keys(Keys.RETURN)

	def click_login(self):
		bpe=BasePageElements(self.driver)
		bpe.click_login_link()

class LoginPage():
	def __init__(self,driver):
		self.driver=driver

	def login(self,username,password):
		lpe=LoginPageElements(self.driver)
		utb=lpe.username()
		utb.send_keys(username)
		utb.send_keys(Keys.RETURN)
		ptb=lpe.password()
		ptb.send_keys(password)
		lpe.signin().click()

class SearchResultsPage(BasePage):
	def Results_Check(self):
		return "No results found" not in self.driver.page_source

class UserPage(LoginPage):
	def Userpage_Check(self):
		return "divya" in self.driver.page_source

