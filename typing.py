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
		driver.get("http://manabi.benesse.ne.jp/gakushu/typing/nihongonyuryoku.html")
		driver.find_element_by_xpath("//button[@id='goSettingButton']").click()
		driver.find_element_by_xpath("//div[3]/button").click()
		driver.find_element_by_tag_name("body").send_keys(Keys.SPACE)

		print("スタート")
		ans = driver.find_element_by_tag_name("body")
		while True:
			text = driver.find_element_by_xpath("//span[@id='remaining']").text
			ans.send_keys(text)

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

