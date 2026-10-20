from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    def ingresar_usuario(self,usuario):
       self.driver.find_element(By.ID, "user-name")
       self.driver.find_element(By.ID, "password")
       self.driver.find_element(By.ID, "login-button")
