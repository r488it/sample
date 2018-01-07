# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import datetime


class LoginLogout(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()

###################################################################
	def test_login_logout(self):
		driver = self.driver
		driver.get("http://www.speedsums.com/")
		for i in range(119):
			question = driver.find_element_by_xpath("//div[@id = 'question']")
			ans= eval(question.text.replace("=","").replace("x","*").replace("÷","/"))
			print(question.text,int(ans))
			answer = driver.find_element_by_xpath("//input[@id = 'answer']")
			answer.clear()
			answer.send_keys(int(ans))

###################################################################
	def is_element_present(self, how, what):
		pass

	def is_alert_present(self):
		pass

	def close_alert_and_get_its_text(self):
		pass

	def tearDown(self):
		pass

if __name__ == "__main__":
	unittest.main()

