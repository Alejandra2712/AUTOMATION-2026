from behave import given,when,then
from pages.login_page import LoginPage

@given("que el usuario se encuentre en la pagina del login")
def step_usuario_en_login(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.abrir_pagina()
    
@when('ingresa en los campos "{usuario}" y "{contrasena}"')
def step_ingresar_credenciales(context, usuario, contrasena):
    context.login_page.ingresar_usuario(usuario)
    context.login_page.ingresar_password(contrasena)
    
@when("hace clic en el boton de login")
def step_hacer_click_login(context):
    context.login_page.hacer_click_en_login()

@then("el usuario debería ingresar al inventario")
def step_validar_login_exitoso(context):
    assert "/inventory.html" in context.driver.current_url

@then('deberia mostrarse el mensaje de error "{mensaje}"')
def step_validar_mensaje_error(context, mensaje):
    error = context.login_page.obtener_mensaje_error()
    print(error)
    assert mensaje in error, f"Se esperaba {mensaje}, pero se obtuvo {error}"
    
    