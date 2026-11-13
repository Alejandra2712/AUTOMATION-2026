Feature: Inicio de sesión
    Background:
        Given que el usuario se encuentre en la pagina del login
        
    Scenario: Inicio de sesión exitoso
        When ingresa en los campos "standard_user" y "secret_sauce"
        And hace clic en el boton de login
        Then el usuario debería ingresar al inventario

    Scenario: Login invalido con contraseña incorrecta
        When ingresa en los campos "standard_user" y "1234"
        And hace clic en el boton de login
        Then deberia mostrarse el mensaje de error "Epic sadface: Username and password do not match any user in this service"

    Scenario Outline: Login invalido con diferentes credenciales
        When ingresa en los campos "<usuario>" y "<password>"
        And hace clic en el boton de login
        Then deberia mostrarse el mensaje de error "<mensaje>"

        Example:
        |usuaro|password|mensaje|
        |standard_user|1234|Epic sadface: Username and password do not match any user in this service|
        |standart_user│secret_sauce│Epic sadface: Username and password do not match any user in this service│
        |secret_sauce|Epic sadface: Username is required|
        │standard_user| |Epic sadface: Password is required|