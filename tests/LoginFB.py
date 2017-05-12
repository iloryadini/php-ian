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
handler_critical = logging.FileHandler('LoginFB.txt','w')
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
		Hover = ActionChains(driver).move_to_element(SearchButton)
		Hover.perform()
		# time.sleep (1)
		#class="qeon__dropdown qeon__dropdown--member qeon__dropdown--m__content show-container"
		LogoutButton = driver.find_element_by_xpath('/html/body/header/div/div[2]/div/div[2]/div/div/ul/li[3]/a').click()
		logger.info	("-----Logout Success-----")

	def tearDown(self):
		self.driver.quit()
		logger.info	("-----End Of Test, Please Check LoginQeon.TXT For Check Error -----")
if __name__ == "__main__":
	unittest.main()