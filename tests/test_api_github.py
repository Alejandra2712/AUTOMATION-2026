# Esta es una prueba ejemplo que esta en la clase 11. El código tal como esta en líneas 6-14 se ejecuta con "run". E
# En cambio, si lo pruebo con Pytest, necesito que esté en una función, con los asserts necesarios, como está en
# las líneas 19-26


import requests 
# 1) Hacemos la solicitud HTTP 
resp = requests.get('https://api.github.com')
# 2) Imprimimos el código de estado 
print(resp.status_code) # 200 = OK 
# 3) Vemos el tipo de contenido devuelto 
print(resp.headers['content-type']) # application/json

# 4) Convertimos el JSON a dict de Python 
payload = resp.json() 
print(payload['current_user_url'])


def test_api_github():
    resp = requests.get("https://api.github.com", timeout=10)

    assert resp.status_code == 200
    assert "application/json" in resp.headers["content-type"]

    payload = resp.json()
    assert "current_user_url" in payload 