from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import unittest
import logging

#create a logger
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

# #create log-handlers
# #I need the critical logs in a file called Youtube.txt
# handler_critical = logging.FileHandler('contact.txt')
# handler_critical.setLevel(logging.WARNING)
# #I need all the logs above the INFO level on the console
# handler_info = logging.StreamHandler()
# handler_info.setLevel(logging.INFO)

# #FORMATTERES
# formatter = logging.Formatter('%(asctime)s - %(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler_critical.setFormatter(formatter)
# handler_info.setFormatter(formatter)

# #add the handlers
# logger.addHandler(handler_info)
# logger.addHandler(handler_critical)
client_urls = ['http://qaflowerstudio.qeon.co.id/contact-us' , 'http://qaqdh.qeoninteractive.com/#contact']
# element_client = ['name' , 'email' , 'phone' , 'comment' ,'company' ,'telp']
class ContactUs(unittest.TestCase):
	def setUp(self):

		# for browser in browsers:
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.implicitly_wait(5)
		# self.driver.get('http://qaflowerstudio.qeon.co.id/contact-us')
		for asd in client_urls:
			self.driver.get(asd)
			self.test_ContactUs()
			# driver = self.driver
			# driver.find_element_by_name('name').send_keys('qaqeon')
			# driver.find_element_by_name('email').send_keys('qadev@qeon.co.id')
			# self.driver.get(client_urls)
		
	def test_ContactUs(self):
		driver = self.driver
		driver.find_element_by_name('name').send_keys('qaqeon')
		driver.find_element_by_name('email').send_keys('qadev@qeon.co.id')

	def tearDown(self):
		self.driver.quit()
		
if __name__ == "__main__":
	unittest.main()