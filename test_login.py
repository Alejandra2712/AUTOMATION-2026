
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_exitoso():
    #Abrir el navegador que quiero
    driver = webdriver.Chrome()
    
    driver.implicitly_wait(10) #Tiempo de espera implicito para que el driver espere a que los elementos estén disponibles
    
    try: #Abrir el login de la página
        driver.get("https://www.saucedemo.com")
        
        usuario = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        boton_login = driver.find_element(By.ID, "login-button")

        #Completar el formulario de login

        usuario.send_keys("standard_user")
        time.sleep(1)
        password.send_keys("secret_sauce")
        time.sleep(1)

        #Hacer click en el botón de login

        boton_login.click()
        time.sleep(1)
    
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
    



