#x-api-key":"pub_58272708b77872738d5672da842f290a5408786869b4d947cc49"

import requests
import pytest_check as check

def test_obtener_usuario():
    url = "https://reqres.in/api/users/2"
    header = {        
        "x-api-key": "pub_58272708b77872738d5672da842f290a5408786869b4d947cc49d4f1ab3cf70f"
        
    } # los headers son pares clave valor para enviar datos sobre la peticion 
    response = requests.get(url,headers=header)
    
    #Nivel 1_ Status code
    codigo = response.status_code 
    assert codigo == 200
   
    #Nivel 2: Headers
    assert"application/json" in response.headers["Content-Type"]
    
    #Nivel 3: Estructura
    data = response.json()    
     
    assert isinstance(data, dict) # Validar que sea un diccionario
    assert "data" in data
    assert isinstance(data["data"], dict) # Validar que sea un diccionario
    assert "id" in data["data"]
    assert "email" in data["data"]
    assert "first_name" in data["data"]    
    assert "last_name" in data["data"]
    
    #Nivel 4: Contenido
    assert data["data"]["id"] == 2
    assert data["data"]["email"] == "janet.weaver@reqres.in"
    
    #Nivel 5: Tiempo de respuesta    
    assert response.elapsed.total_seconds() < 2  # Validar que la respuesta sea rápida

def test_crear_usuario():
    url = "https://reqres.in/api/users"
    header = {
        "x-api-key": "pub_58272708b77872738d5672da842f290a5408786869b4d947cc49d4f1ab3cf70f"
    }
    
    usuario = {
        "email": "silvia.cespedes@bue.edu.ar",
        "first_name": "Silvia",
        "last_name": "Cespedes",
        "job": "leader"
    }
    response = requests.post(url, headers=header,json=usuario)
    
    #Nivel 1_ Status code
    assert response.status_code == 201
   
    #Nivel 2: Headers
    assert"application/json" in response.headers["Content-Type"]
    
    #Nivel 3: Estructura
    data = response.json()    
    check.is_in("email",data)# assert "email" in data
    check.is_in("first_name",data)# assert "first_name" in data
    check.is_in("last_name",data)# assert "last_name" in data    
    check.is_in("id",data)# assert "id" in data
    
    #Nivel 4: Contenido
    check.is_in(data["email"],usuario["email"])# assert data["email"] == usuario["email"]
    check.is_in(data["first_name"],usuario["first_name"])# assert data["first_name"] == usuario["first_name"]
    
    #Nivel 5: Tiempo de respuesta    
    assert response.elapsed.total_seconds() < 2  # Validar que la respuesta sea rápida
    
# test_obtener_usuario()