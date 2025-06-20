# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC

from Tests.configs import Logar

class TestDeslogar():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_deslogar(self):
    driver = Logar(self.driver)
    driver.find_element(By.CSS_SELECTOR, ".btn-header:nth-child(3) > .btn").click()

    WebDriverWait(driver, 10).until(
      EC.url_contains("dash")
    )
    
    WebDriverWait(self.driver, 10).until(
      EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-header:nth-child(1) > .btn"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("login")
    )

    assert "login" in driver.current_url
  
