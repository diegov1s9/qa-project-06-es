import configuration
import requests
import data
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)
#Lineas comentadas ya que solo se utilizan solo para validar la funcion post_new_user en caso de error
#response = post_new_user(data.user_body)
#print("status_code: " + str(response.status_code) + " response: " + str(response.json()))

def post_new_client_kit(kit_body):
    #Creo un usuario en base data.user_body
    response_post_new_user = post_new_user(data.user_body)
    #Almaceno el auth_token del usuario creado
    auth_token = response_post_new_user.json()["authToken"]
    #Obtengo los headers base del archivo data.py
    current_headers = data.headers.copy()
    #Actualizo el Authorization con un authToken valido del usuario creado
    current_headers["Authorization"] = current_headers["Authorization"] + auth_token
    #retorno el resultado
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=current_headers)
#Lineas comentadas ya que se utilizan para validar funcion post_new_client_kit utilizando datos de data.kit_body
#response = post_new_client_kit(data.kit_body)
#print("status_code: " + str(response.status_code) + " response: " + str(response.json()))