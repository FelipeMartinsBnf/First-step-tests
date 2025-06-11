from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Tests.configs import Logar

# Teste para verificar se é possível logar e cair na página de dashboard

class TestLogin():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_login(self):
    driver = Logar(self.driver)
    driver.find_element(By.CSS_SELECTOR, ".btn-header:nth-child(3) > .btn").click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("dash")
    )

    assert "dash" in driver.current_url
  
