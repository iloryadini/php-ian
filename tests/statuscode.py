from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import requests

class PythonOrgSearch(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome() # buat panggil browser
		self.driver.maximize_window()
		self.driver.implicitly_wait(5)
		self.driver.get("https://accounts.qeon.com")
	def test_openWeb(self):
		driver = self.driver
		r = requests.get("https://accounts.qeon.com")
		self.print (r.status_code)

	def tearDown(self):
		self.driver.quit() # buat close browser

if __name__ == "__main__":
	unittest.main()