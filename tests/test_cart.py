import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_cart():
    #Abrir el navegador que quiero
    driver = webdriver.Chrome()
    wait= WebDriverWait(driver, 10)  # Tiempo de espera explícito para esperar a que los elementos estén disponibles
    
    driver.implicitly_wait(10) #Tiempo de espera implicito para que el driver espere a que los elementos estén disponibles
    
    try: #Abrir el login de la página
        
        driver.get("https://www.saucedemo.com")
        
        wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")  # Esperar a que el campo de usuario sea visible o...
        # usuario = driver.find_element(By.ID, "user-name")
        
        password = driver.find_element(By.ID, "password")
        boton_login = driver.find_element(By.ID, "login-button")
        password.send_keys("secret_sauce")
        
        boton_login.click()
        
        primer_producto = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item")))  # Esperar a que los productos sean visibles
        nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
        botón_agregar = primer_producto.find_element(By.TAG_NAME, "button")
        
        botón_agregar.click()
        
        contador_carrito = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))  # Esperar a que el contador del carrito sea visible    
        assert contador_carrito.text == "1"
        
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()  # Esperar a que el enlace del carrito sea clickeable y hacer click
        nombre_producto_carrito = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))).text # Esperar a que el producto en el carrito sea visible
        assert nombre_producto_carrito == nombre_producto

    finally:
        driver.quit()