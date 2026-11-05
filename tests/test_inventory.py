from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_inventory(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    
    #Abrir el login de la página
    driver.get("https://www.saucedemo.com")
    
    login_page.login("standard_user", "secret_sauce")
    
    # Esta línea provoca un fallo intencional para probar el hook
    # assert False, "Fallo controlado para probar la captura"
           
    productos = inventory_page.obtener_productos()
    
    assert len(productos) > 0
    assert inventory_page.obtener_nombre_primer_producto() == "Sauce Labs Backpack"
    assert inventory_page.obtener_precio_primer_producto() == "$29.99"      
    assert inventory_page.menu_visible()
    assert inventory_page.filtro_visible()