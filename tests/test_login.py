
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_login_exitoso():
    #Abrir el navegador que quiero
    driver = webdriver.Chrome()
    
    driver.implicitly_wait(10) #Tiempo de espera implicito para que el driver espere a que los elementos estén disponibles
    
    wait = WebDriverWait(driver, 10)  # Tiempo de espera explícito para esperar a que los elementos estén disponibles   
    
    try: #Abrir el login de la página
        driver.get("https://www.saucedemo.com")
        
        usuario = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        boton_login = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))

        #driver.find_element(By.ID, "login-button")
        
        usuario.send_keys("standard_user")
        password.send_keys("secret_sauce")
        
        #Hacer click en el botón de login

        boton_login.click()
        
    
        #Validar URL de la página de productos despues del login
        # assert driver.current_url == "https://www.saucedemo.com/inventory.html"
        
        assert "/inventory.html" in driver.current_url
        
        #Validar texto
        logo = driver.find_element(By.CLASS_NAME, "app_logo")
        assert logo.text == "Swag Labs"
        
        titulo = driver.find_element(By.CSS_SELECTOR,"[data-test='title']")
        assert titulo.text == "Products"
    
    finally:
        driver.quit()
    



