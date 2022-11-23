# Generated by Selenium IDE
import pytest
import time
import json
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestSeoallintitle():
  
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
      
    def teardown_method(self, method):
        self.driver.quit()

    def test_seoallintitle(self):
        self.driver.get("https://www.google.com/webhp")
        self.driver.set_window_size(1050, 702)
        self.bypass_accept_cookie()
        self.all_keywords()
        
    def bypass_accept_cookie(self):
        # TODO: find more stable way, because id could change
        self.driver.find_element(By.ID, "L2AGLb").click()

    def get_keywords(self):
        return [
          "keyword1",
          "keyword2",
          "keyword3",
          "keyword4",
          "keyword5",
          "keyword6",
        ]

    def all_keywords(self):
        for keyword in self.get_keywords():
            self.get_result_for_all_keywords(keyword) 

    def get_result_for_all_keywords(self, keyword):
        self.driver.find_element(By.NAME, "q").send_keys("allintitle: {}".format(keyword))
        self.driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
        element = self.driver.find_element(By.ID, "result-stats")
        text = element.text
        pattern = r"Environ (.*) résultats" 
        resultat = re.match(pattern, text)
        print(resultat.groups()[0].replace("\u202f", ""))
