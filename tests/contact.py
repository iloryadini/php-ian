from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import unittest
import logging
import sys
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
client_urls = ['http://qaqdh.qeoninteractive.com/#contact' , 'http://qaflowerstudio.qeon.co.id/contact-us']

# phones = ['phone' , 'telp']
# pesan = ['comment' , 'message']
# element_client = ['name' , 'email' , 'phone' , 'comment' ,'company' ,'telp']
class ContactUs(unittest.TestCase):
	def setUp(self):

		# for browser in browsers:
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.implicitly_wait(20)
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
		# time.sleep(1)
		driver.find_element_by_name('email').send_keys('qadev@qeon.co.id')
		# time.sleep(1)
		if "No.Telp" in driver.page_source:
			driver.find_element_by_name('telp').send_keys('081234567')
		else:
			driver.find_element_by_name('phone').send_keys('081234567')
		# time.sleep(1)
		if "qdh" in driver.page_source:
			driver.find_element_by_name('message').send_keys('Sorry for spamming once a week, this is automatic test. Please Dont Reply This email')
		else:
			driver.find_element_by_name('comment').send_keys('Sorry for spamming once a week, this is automatic test. Please Dont Reply This email')
		# time.sleep(1)
		if "Company" in driver.page_source:
			driver.find_element_by_name('company').send_keys('PT QA QEON INTERACTIVE')
		else:
			return
		# time.sleep(2)
		if "contactUs-button" in driver.page_source:
			driver.find_element_by_class_name('btn--main').click()
		else:
			driver.find_element_by_class_name('btn--main__small').click()
		return
		# time.sleep(2)
		driver.find_element_by_partial_link_text('SUBMIT').click()
	def tearDown(self):
		self.driver.quit()
		
if __name__ == "__main__":
	unittest.main()