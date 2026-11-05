Feature: Inicio de sesión
    Scenario: Inicio de sesión exitoso
        Given que el usuario se encuentre en la pagina del login
        When ingresa en los campos "standard_user" y "secret_sauce"
        And hace clic en el botón de login
        Then el usuario debería ingresar al inventario
