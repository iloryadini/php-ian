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
handler_critical = logging.FileHandler('LoginQeon.txt','w')
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

class LoginQeon(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.implicitly_wait(5)
		self.driver.get('https://accounts.qeon.com')


	def test_loginSuccess(self):
		driver = self.driver
		logger.info	("-----start Login With Username-----")
		# driver.get('https://accounts.qeon.com')
		driver.find_element_by_name("uname").send_keys("ianianian")
		#time.sleep (2)
		driver.find_element_by_name("passwd").send_keys("mynameisian")
		#time.sleep (2)
		driver.find_element_by_name("login").click()
		try:
			self.assertEqual("https://accounts.qeon.com/account/settings", driver.current_url)
		except AssertionError as error_huft:#time.sleep (2)
			logger.critical('Hasil URL nya berbeda',exc_info=True)
		logger.info	("-----Login Username Success-----")
		SearchButton = driver.find_elements_by_class_name("qeon__anchor--dropdown")[3]
		#print(len(SearchButton))
		Hover = ActionChains(driver).move_to_element(SearchButton)
		Hover.perform()
		#time.sleep (2)
		#class="qeon__dropdown qeon__dropdown--member qeon__dropdown--m__content show-container"
		LogoutButton = driver.find_element_by_xpath('/html/body/header/div/div[2]/div/div[2]/div/div/ul/li[3]/a').click()
		logger.info	("-----Logout Success-----")

	def test_LoginGoogle(self):
		driver = self.driver
		# driver.get('https://accounts.qeon.com')
		logger.info	("-----start Login Google-----")
		driver.find_element_by_class_name("button--gplus").click()
		time.sleep(1)
		driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys("xiewey1")
		time.sleep(1)
		driver.find_element_by_id("identifierNext").click()
		time.sleep(1)
		driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys("qeon12345")
		time.sleep(1)
		driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span').click()
		time.sleep(1)
		try:
			self.assertEqual("https://accounts.qeon.com/account/settings#", driver.current_url)
			time.sleep(1)
		except AssertionError as error_huft:
			logger.critical('Hasil URL nya berbeda',exc_info=True)
		logger.info	("-----Login With Google Success-----")
		
		SearchButton = driver.find_elements_by_class_name("qeon__anchor--dropdown")[3]
		time.sleep(2)
		#print(len(SearchButton))
		Hover = ActionChains(driver).move_to_element(SearchButton)
		Hover.perform()
		#time.sleep (2)
		#class="qeon__dropdown qeon__dropdown--member qeon__dropdown--m__content show-container"
		LogoutButton = driver.find_element_by_xpath('/html/body/header/div/div[2]/div/div[2]/div/div/ul/li[3]/a').click()
		logger.info	("-----Logout Success-----")

	def test_LoginFacebook(self):
		driver = self.driver
		logger.info	("-----Start Login with Facebook Success-----")
		# driver.get('https://accounts.qeon.com')
		driver.find_element_by_class_name("button--facebook").click()
		time.sleep(1)
		driver.find_element_by_id("email").send_keys("xiewey1@gmail.com")
		driver.find_element_by_id("pass").send_keys("qeon12345")
		driver.find_element_by_id("loginbutton").click()
		time.sleep(2)
		try:
			self.assertEqual("https://accounts.qeon.com/account/settings#_=_", driver.current_url)
			time.sleep(1)
		except AssertionError:
			logger.critical('Hasil URL nya berbeda',exc_info=True)
		SearchButton = driver.find_elements_by_class_name("qeon__anchor--dropdown")[3]
		#print(len(SearchButton))
		# time.sleep(1)
		time.sleep(2)
		Hover = ActionChains(driver).move_to_element(SearchButton)
		Hover.perform()
		# time.sleep (1)
		#class="qeon__dropdown qeon__dropdown--member qeon__dropdown--m__content show-container"
		LogoutButton = driver.find_element_by_xpath('/html/body/header/div/div[2]/div/div[2]/div/div/ul/li[3]/a').click()
		logger.info	("-----Logout Success-----")

	def test_AccountNotRegistered(self):
		logger.info	("-----Start Login Fail Account Not Registered-----")
		driver = self.driver
		# driver.get('https://accounts.qeon.com') # url awal
		driver.find_element_by_name("uname").send_keys("asdfasdf") # input form nya di cari by name form nya tersebut, dan send_keys buat input isi formnya 
		time.sleep (1)
		driver.find_element_by_name("passwd").send_keys("asdfsadf")
		time.sleep (1)
		driver.find_element_by_name("login").click()
		time.sleep (1)
		try:
			assert "The account has not been registered" in driver.page_source #untuk pengecekan kata2 "The account has not been registered" ada di source page, klo ga ada dia munculin error
		except AssertionError as error_huft:
			logger.critical('Tidak ada kata kata account has not been registered', exc_info=True)
		logger.info	("-----Login Fail Account Not Registered Success-----")
	def test_PasswordEmpty (self):
		logger.info	("-----Start Login Fail Password Empty-----")
		driver = self.driver
		# driver.get('https://accounts.qeon.com') # url awal
		time.sleep (1)
		# driver.find_element_by_name("uname").clear()
		driver.find_element_by_name("uname").send_keys("ianianian")
		time.sleep (1)
		driver.find_element_by_name("passwd").send_keys()
		time.sleep (1)
		driver.find_element_by_name("login").click()
		time.sleep (1)
		try:
			assert "Password is required" in driver.page_source  #untuk pengecekan kata2 "Password is required" ada di source page, klo ga ada dia munculin error Password does not match
		except AssertionError as error_huft:
			logger.critical('tidak ada kata kata Password is required', exc_info=True)
		logger.info	("-----Login Fail Password Empty Success-----")
	def test_WrongPassword (self):
		logger.info	("-----Start Login Fail Wrong Password-----")
		driver = self.driver
		# driver.get('https://accounts.qeon.com') # url awal
		time.sleep (1)
		# driver.find_element_by_name("uname").clear()
		driver.find_element_by_name("uname").send_keys("ianianian")
		time.sleep (1)
		driver.find_element_by_name("passwd").send_keys("adsfasfasf")
		time.sleep (1)
		driver.find_element_by_name("login").click()
		time.sleep (1)
		try:
			assert "Password does not match" in driver.page_source  #untuk pengecekan kata2 " Password does not match" ada di source page, klo ga ada dia munculin error
		except AssertionError as error_huft:
			logger.critical('Tidak ada kata kata password does not match', exc_info=True)
		logger.info	("-----Login Fail Wrong Password Success-----")

	def tearDown(self):
		self.driver.quit()
		
if __name__ == "__main__":
	unittest.main()