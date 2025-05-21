from selenium import webdriver
from selenium.webdriver.common.by import By
from Tests.configs import Logar


class TestLogin():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_login(self):
    driver = Logar(self.driver)
    driver.find_element(By.CSS_SELECTOR, ".btn-header:nth-child(3) > .btn").click()
    assert "dash" in driver.current_url
  
