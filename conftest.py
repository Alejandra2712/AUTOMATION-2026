import pathlib
import base64
import pytest
from selenium import webdriver
import pytest_html

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")  # Ejecutar en modo headless (sin interfaz gráfica)
    options.add_argument("--incognito") # Ejecutar en modo incógnito
    driver = webdriver.Chrome(options=options)
    
    driver.implicitly_wait(10)
      
    yield driver
    driver.quit()

   
@pytest.fixture
def base_url():
    return "https://regres.in/api" 

@pytest.fixture
def headers():
    return {"x-api-key": "pub_58272708b77872738d5672da842f290a5408786869b4d947cc49d4f1ab3cf70f"}

#Tomar captura de pantalla cuando falle un test
    
@pytest.hookimpl(hookwrapper=True) # Este bloque hookimpl se puede usar para cualquier prueba.
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        
        carpeta = pathlib.Path("reports/screenshots")
        carpeta.mkdir(parents=True,exist_ok=True)
        archivo = carpeta / f"{item.name}.png"
        
        driver.save_screenshot(str(archivo))
        
        #Incrustar imagen en html
        
        imagen =base64.b64encode(archivo.read_bytes()).decode("utf-8")
        report.extras = [
            pytest_html.extras.png(imagen, name="Screenshot")
            ]