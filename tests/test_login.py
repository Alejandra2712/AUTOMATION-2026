from pages.login_page import LoginPage
import pytest
from utils.reader import read_users_csv
from utils.logger import logger


@pytest.mark.parametrize(
    "data", read_users_csv())  
       
def test_login_exitoso(driver,data):
    try:
        login_page = LoginPage(driver)
        logger.info("Iniciando prueba de login")
        
        driver.get("https://www.saucedemo.com")
        logger.info("Página de login abierta")
            
        login_page.login(data["usuario"], data["password"])
        logger.info("Ingreso de credenciales")
        
        if data["tipo_usuario"] == "user_ok":
            
            #Validar URL de la página de productos despues del login
            assert "/inventory.html" in driver.current_url
            logger.info("Login exitoso")
        elif data["tipo_usuario"] == "user_fail":
            error = login_page.obtener_mensaje_error()
            print(error)
            
            #Validar mensaje de error
            assert "Epic sadface" in error
            logger.info("Prueba de mensaje de error válida")
    except Exception:
        logger.exception("Error durante la prueba de login")
        raise
        
    