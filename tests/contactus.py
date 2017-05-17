from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import unittest
import logging

#create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#create log-handlers
#I need the critical logs in a file called Youtube.txt
handler_critical = logging.FileHandler('contactus.txt')
handler_critical.setLevel(logging.WARNING)
#I need all the logs above the INFO level on the console
handler_info = logging.StreamHandler()
handler_info.setLevel(logging.INFO)

#FORMATTERES
formatter = logging.Formatter('%(asctime)s - %(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler_critical.setFormatter(formatter)
handler_info.setFormatter(formatter)

#add the handlers
logger.addHandler(handler_info)
logger.addHandler(handler_critical)
client_urls = ['http://qaflowerstudio.qeon.co.id/contact-us' , 'http://qaqdh.qeoninteractive.com/#contact']
# browsers = ['Chrome','Firefox']
# flowerstudio = 'http://qaflowerstudio.qeon.co.id/contact-us'
# qdh = 'http://qaqdh.qeoninteractive.com/#contact'
# ayana = 'http://qa.ayana.com/contact'
# detik = 'http://inet.detik.com/indeks'
# complete_urls = (client_urls + client_urls)
class ContactUs(unittest.TestCase):
	def setUp(self):
		# for browser in browsers:
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.implicitly_wait(5)
		# for asd in client_urls:
		# 	# self.driver = self.driver.get(asd)
		# 	print (asd)
		# self.driver = self.driver.get(asd)
		# self.flower = self.driver.get(client_urls)
		# self.qdh = self.driver.get(qdh)
		# self.ayana = self.driver.get(flowerstudio)
		# self.detik = self.driver.get(detik)
	def test_ContactUsFlower(self):
	# 	# for asd in client_urls:
	# 	# 	# self.driver = self.driver.get(asd)
	# 	# 	print (asd)
	# 	# self.driver = self.driver.get(asd)
		# driver = self.driver.get(client_urls[0])
		driver = self.driver.get('http://qaflowerstudio.qeon.co.id/contact-us')
		# logger.info	("-----Open Contact Us Flower Studio -----")
		self.driver.find_element_by_name('name').send_keys('qaqeon')
		logger.info	("-----Input Kolom Name -----")
		time.sleep(1)
		self.driver.find_element_by_name('email').send_keys('qadev@qeon.co.id')
		logger.info	("-----Input Kolom Email -----")
		time.sleep(1)
		self.driver.find_element_by_name('phone').send_keys('08123456789')
		logger.info	("-----Input Kolom Phone -----")
		time.sleep(1)
		self.driver.find_element_by_name('comment').send_keys('Sorry for spamming once a week, this is automatic test. Please Dont Reply This email ')
		logger.info	("-----Input Kolom Comment -----")
		self.driver.find_element_by_class_name('btn--main__small').click()
		# driver.find_element_by_class_name('btn--main').click()
		logger.info	("-----Input Send Buttom -----")
		# time.sleep(13)
		# try:
		# 	assert 'Thank you. Your submission was successful and we will get back to you shortly.' in self.driver.page_source
		# except AssertionError:
		# 	logger.critical("Input Form Gagal",exc_info=True)
		# logger.info	("-----Send Form -----")
		

	# def test_ContactUsQDH(self):
	# 	driver = self.driver.get(client_urls[1])
	# 	self.driver.find_element_by_name('name').send_keys('qaqeon')
	# 	logger.info	("-----Input Kolom Name -----")
	# 	time.sleep(1)
	# 	self.driver.find_element_by_name('email').send_keys('qadev@qeon.co.id')
	# 	logger.info	("-----Input Kolom Email -----")
	# 	time.sleep(1)
	# 	self.driver.find_element_by_name('company').send_keys('PT QA QEON INTERACTIVE')
	# 	logger.info	("-----Input Kolom Company -----")
	# 	time.sleep(1)
	# 	self.driver.find_element_by_name('telp').send_keys('08123456789')
	# 	logger.info	("-----Input Kolom telp -----")
	# 	time.sleep(1)
	# 	self.driver.find_element_by_name('message').send_keys('Sorry for spamming once a week, this is automatic test. Please Dont Reply This email')
	# 	logger.info	("-----Input Kolom message -----")
	# 	time.sleep(1)
	# 	self.driver.find_element_by_class_name('btn--main').click()
	# 	logger.info	("-----Input Submit Button -----")
	# 	try:
	# 		assert 'Thank you for your inquiry!' in self.driver.page_source
	# 	except AssertionError:
	# 		logger.critical("Input Form Gagal",exc_info=True)
		
	# def test_ContactUsQDH(self):
	# 	driver = self.ayana
	# 	logger.info	("-----Open Contact Us Ayana -----")
	# 	time.sleep(1)
	# 	self.driver.find_element_by_xpath('//*[@id="contact-us-reason-form-group"]/div/div[1]/div/div/div[2]').click()
	# 	time.sleep(1)
	# 	self.driver.find_element_by_xpath('//*[@id=":1b"]').click()
	# 	logger.info	("-----Choose Meeting dan Event-----")
	# 	time.sleep(1)
	# 	self.driver.find_element_by_xpath('//*[@id="contact-us-mice-form"]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div/div/div[2]').click()
	# 	time.sleep(1)
	# 	self.driver.find_element_by_xpath('//*[@id=":tu"]').click()
	# 	logger.info	("-----Choose Mr.-----")
	# 	time.sleep(1)
	# 	self.driver.find_element_by_xpath('//*[@id="contact-us-mice-email-address"]').send_keys('qadev@qeon.co.id')
	# 	time.sleep(1)
	# 	self.driver.find_element_by_xpath('//*[@id="contact-us-mice-fullname"]').send_keys('QA Qeon')
	# 	time.sleep(1)
	# 	self.driver.find_element_by_xpath('//*[@id="contact-us-mice-contact-number"]').send_keys('08123456789')
	# 	time.sleep(1)
	# 	self.driver.find_element_by_xpath('//*[@id="contact-us-mice-form"]/div[1]/div[1]/div[2]/div[4]/div[1]/div[2]/div/div[1]/div/div/div[2]').click()
	# 	time.sleep(1)
	# 	self.driver.find_element_by_xpath('//*[@id=":wu"]').click()
	# 	logger.info ("----- Choose Country Indonesia ------")
	# 	self.driver.find_element_by_xpath('//*[@id="contact-us-mice-form"]/div[1]/div[1]/div[2]/div[4]/div[3]/div[2]/div/div/div/div/div[2]').click()
	# 	time.sleep(1)
	# 	self.driver.find_element_by_xpath('//*[@id=":13s"]').click()
	# 	logger.info ('----- Choose Residence Indonesia-----')
	# 	time.sleep(1)
	# 	self.driver.find_element_by_xpath('//*[@id="contact-us-mice-address-line-01"]').send_keys('Jl Jendral Sudirman Kav 11-12')
	# 	time.sleep(1)
	# 	self.driver.find_element_by_xpath('//*[@id="contact-us-mice-address-city"]').send_keys('Jakarta')
	# 	time.sleep(1)
	# 	self.driver.find_element_by_xpath('//*[@id="contact-us-mice-address-province"]').send_keys('DKI Jakarta')
	# 	time.sleep(1)
	# 	self.driver.find_element_by_xpath('//*[@id="contact-us-mice-address-postal-code"]').send_keys('12131')
	# 	time.sleep(1)
	# 	self.driver.execute_script("scroll(0, 1250)")
	# 	time.sleep(2)
	# 	self.driver.find_element_by_xpath('//*[@id="contact-us-mice-event-name"]').send_keys('Automatic Testing')
	# 	time.sleep(1)
	# 	self.driver.find_element_by_xpath('//*[@id="contact-us-mice-form"]/div[1]/div[3]/div[2]/div[4]/div[1]/div/div[2]/label/span').click()
	# 	time.sleep(1)
	# 	self.driver.find_element_by_xpath('//*[@id="contact-us-mice-event-participant-number"]').send_keys('12')
	# 	time.sleep(1)

	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()