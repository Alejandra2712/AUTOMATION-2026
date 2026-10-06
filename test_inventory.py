import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.remote.webelement import WebElement

def test_login_exitoso():
    #Abrir el navegador que quiero
    driver = webdriver.Chrome()
    
    try: #Abrir el login de la página
        driver.get("https://www.saucedemo.com")
        
        usuario = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        boton_login = driver.find_element(By.ID, "login-button")

        usuario.send_keys("standard_user")
        time.sleep(1)
        password.send_keys("secret_sauce")
        time.sleep(1)

        boton_login.click()

        time.sleep(1)
    
        #Verificar título de la página
        assert driver.title == "Swag Labs"
        
        productos: list[WebElement] = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(productos) == 6
        
        primer_producto = productos[0]
        nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
        precio_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text
        
        assert nombre_producto == "Sauce Labs Backpack"
        assert precio_producto == "$29.99"
        
        
    
    finally:
        driver.quit()
    