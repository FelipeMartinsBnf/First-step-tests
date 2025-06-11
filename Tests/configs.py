from selenium.webdriver.common.by import By

def Logar(driver):
    driver.get("https://extensao-first-step.vercel.app/")
    #driver.get("http://localhost:5137/")
    driver.set_window_size(1920, 1080)
    driver.find_element(By.CSS_SELECTOR, "a:nth-child(2) > .undefined").click()
    driver.find_element(By.CSS_SELECTOR, ".input-card-div:nth-child(1) > .input-card-input").click()
    driver.find_element(By.CSS_SELECTOR, ".input-card-div:nth-child(1) > .input-card-input").send_keys("felipemartinsbn@gmail.com")
    driver.find_element(By.CSS_SELECTOR, ".input-card-div:nth-child(2) > .input-card-input").send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(3)").click()
    return driver