from POM.Pages import *
from selenium import webdriver
import unittest
import time
from selenium.webdriver.chrome.options import Options

class testPage(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--no-sandbox')  # # Bypass OS security model
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        options.add_argument("--start-fullscreen")
        options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(executable_path='C:\\Users\\srifo\\chromedriver_win32\\chromedriver.exe')
        self.driver.get('http://www.amazon.com')

    def test_Login(self):
        bpe=BasePageElements(self.driver)
        bpe.click_login_link()
        lp = LoginPage(self.driver)
        lp.login("userid", "password")
        up = UserPage(self.driver)
        self.assertTrue(up.Userpage_Check())

    def test_Search(self):
        bp = BasePage(self.driver)
        bp.search_text("lenovo")
        srp=SearchResultsPage(self.driver)
        self.assertTrue(srp.Results_Check())

    def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(testPage)
    unittest.TextTestRunner(verbosity=2).run(suite)
