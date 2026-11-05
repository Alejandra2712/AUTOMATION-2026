from selenium import webdriver
from selenium.webdriver.common.by import By

def before_scenario(context, scenario):
    # Configurar el navegador antes de cada escenario
    context.driver = webdriver.Chrome()  # Puedes cambiar a otro navegador si lo deseas
    context.driver.maximize_window()

def after_scenario(context, scenario):
    # Cerrar el navegador después de cada escenario
    context.driver.quit()