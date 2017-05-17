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

url = "http://qabiznethotspot.qeon.co.id/?username=6e6577686f7473706f74&password=62697a6e65743939686f7473706f74&loc=00000-MCD02-02-01&uip=10.9.10.98&client_mac=c0:ee:fb:a0:0a:3c&ssid=@FreeBiznetHotspot&starturl=http://qabiznethotspot.qeon.co.id"

class FlashadsCap(unittest.TestCase):
	def setUp(self):
		# for browser in browsers:
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.implicitly_wait(5)
		count = 0
		while (count < 12):
			count = count + 1
			self.driver.get(url)
			self.test_FlasadsCapRedirect()
		# for asd in client_urls:
		# 	# self.driver = self.driver.get(asd)
		# 	print (asd)
		# self.driver = self.driver.get(asd)
		# self.flower = self.driver.get(client_urls)
		# self.qdh = self.driver.get(qdh)
		# self.ayana = self.driver.get(flowerstudio)
		# self.detik = self.driver.get(detik)
	def test_FlasadsCapRedirect(self):
		driver = self.driver
		time.sleep(20)

	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()