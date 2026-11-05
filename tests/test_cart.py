from selenium import webdriver
from conftest import driver
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

from utils.reader import read_productos_json


def test_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver) 
    cart_page = CartPage(driver)
    
    driver.get("https://www.saucedemo.com")

    login_page.login("standard_user", "secret_sauce")
    
    #Leer el primer producto del JSON    
    producto = read_productos_json()[0]
    
    # Agregar el producto del JSONal carrito
    inventory_page.agregar_productos(producto["name"])
    
    assert inventory_page.obtener_contador_carrito() == "1"
    
    #Ir al carrito
    inventory_page.ir_al_carrito()
    
    #Validar nombre contra el JSON
    assert cart_page.obtener_nombre_producto() == producto["name"]
    
    #Validar precio contra el JSON
    assert cart_page.obtener_precio_producto() == producto["price"]
    