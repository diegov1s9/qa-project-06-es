import sender_stand_request
import data

def get_kit_body(name):
    # el diccionario que contiene el cuerpo de solicitud se copia del archivo "data" (datos) para conservar los datos del diccionario de origen
    current_kit_body = data.kit_body.copy()
    # Se cambia el valor del parámetro name
    current_kit_body["name"] = name
    # Se devuelve un nuevo diccionario con el valor name requerido
    return current_kit_body
def positive_assert(name):
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = get_kit_body(name)
    #El resultado de la solicitud para crear un nuevo kit
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    #Comprueba si el código de estado es 201
    assert kit_response.status_code == 201
    #Comprueba que el campo "name" del cuerpo de la respuesta coincide con el de la solicitud
    assert kit_response.json()["name"] == name

def negative_assert_code_400(name):
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = get_kit_body(name)
    # El resultado de la solicitud para crear un nuevo kit
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    # Comprueba si el código de estado es 400
    assert kit_response.status_code == 400
    # Comprueba si el atributo "code" en el cuerpo de respuesta es 400
    assert kit_response.json()["code"] == 400
    # Esta comentada esta validación ya que el mensaje indica de 2 a 15 caracteres, pero el ejercicio indica de 1 a 511 caracteres
    # Comprueba si el atributo "message" en el cuerpo de respuesta se ve así:
    # assert kit_response.json()["message"] == "El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres"

#Prueba 1. Creación de un kit
#El parámetro "name" contiene 1 carácter
def test_create_kit_1_letter_in_name_get_succes_response():
    positive_assert(data.one_character)

#Prueba 2. Creación de un kit
#El parámetro "name" contiene 511 caracteres
def test_create_kit_511_letters_in_name_get_succes_response():
    positive_assert(data.five_hundred_eleven_characters)

#Prueba 3. Creación de un kit
#El parámetro "name" contiene un string vacío ""
def test_create_kit_empty_string_in_name_get_error_respopnse():
    negative_assert_code_400(data.empty_string)

#Prueba 4. Creación de un kit
#El parámetro "name" contiene 512 caracteres número mayor a los permitidos (511)
def test_create_kit_512_letters_in_name_get_error_respopnse():
    negative_assert_code_400(data.five_hundred_twelve_characters)

#Prueba 5. Creación de un kit
#El parámetro "name" contiene caracteres especiales ""№%@","
def test_create_kit_special_characters_in_name_get_succes_response():
    positive_assert(data.special_characters)

# Prueba 6. Creación de un kit
# El parámetro "name" contiene espacios " A Aaa "
def test_create_kit_spaces_in_name_get_succes_response():
    positive_assert(data.string_with_spaces)

# Prueba 7. Creación de un kit
# El parámetro "name" contiene números "123"
def test_create_kit_numbers_in_name_get_succes_response():
    positive_assert(data.string_with_numbers)

# Prueba 8. Creación de un kit
# El parámetro "name" no se pasa en la solicitud
def test_create_kit_name_is_not_passed_get_error_response():
    # El resultado de la solicitud para crear un nuevo kit
    kit_response = sender_stand_request.post_new_client_kit('')
    # Comprueba si el código de estado es 400
    assert kit_response.status_code == 400
    # Comprueba si el atributo "code" en el cuerpo de respuesta es 400
    assert kit_response.json()["code"] == 400

# Prueba 9. Creacion de un kit
# El parámetro "name" contiene un valor numérico
def test_create_kit_name_is_numeric_get_error_response():
    negative_assert_code_400(data.is_numeric)