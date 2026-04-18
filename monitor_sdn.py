import requests
import unittest

# ==========================================
# PARTE 1: Función para consumir la API
# ==========================================
def obtener_info_dispositivo(device_id):
    """
    Simula la consulta a un controlador SDN (o a Cisco DNA Center).
    Consume una API REST y devuelve los datos del dispositivo en formato JSON.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{device_id}"
    
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status() # Lanza una excepción si el status HTTP es de error
        return respuesta.json()      # Retorna el JSON parseado (normalmente un diccionario)
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
        return None


# ==========================================
# PARTE 2: Clase de Pruebas Unitarias
# ==========================================
class TestControladorSDN(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """
        setUpClass se ejecuta una vez antes de todas las pruebas.
        Realizamos la llamada a la API aquí para no sobrecargar el endpoint
        haciendo la misma petición en cada prueba individual.
        """
        # Utilizaremos el ID 1 como nuestro "dispositivo de prueba maestro"
        cls.device_id = 1
        cls.datos_dispositivo = obtener_info_dispositivo(cls.device_id)

    def test_validacion_tipo_dato(self):
        """
        Validación de Tipo de Dato:
        Comprobar que la función devuelva un diccionario (objeto JSON analizado)
        y no una lista o cadena simple.
        """
        # Verificamos que los datos no sean nulos por un error de conexión
        self.assertIsNotNone(self.datos_dispositivo, "La API no devolvió datos.")
        
        # Verificamos que sea un diccionario
        self.assertIsInstance(self.datos_dispositivo, dict, 
                              "El resultado devuelto no es un diccionario válido.")

    def test_validacion_integridad_atributos(self):
        """
        Validación de Integridad de Atributos:
        Verificar que el objeto contenga una clave esencial para la gestión SDN.
        """
        claves_esenciales = ['id', 'username', 'email']
        
        for clave in claves_esenciales:
            self.assertIn(clave, self.datos_dispositivo, 
                          f"El objeto JSON carece de la clave esencial: '{clave}'")

    def test_validacion_valor_esperado(self):
        """
        Validación de Valor Esperado:
        Confirmar que, para el ID 1, el valor del campo coincida con el registro maestro.
        (En JSONPlaceholder, el usuario con ID 1 tiene el username 'Bret').
        """
        valor_id_esperado = 1
        valor_username_esperado = 'Breta' # Valor maestro conocido para este ID
        
        self.assertEqual(self.datos_dispositivo['id'], valor_id_esperado, 
                         f"El ID no coincide. Esperado: {valor_id_esperado}, Obtenido: {self.datos_dispositivo.get('id')}")
        
        self.assertEqual(self.datos_dispositivo['username'], valor_username_esperado, 
                         f"El username no coincide. Esperado: {valor_username_esperado}, Obtenido: {self.datos_dispositivo.get('username')}")


# ==========================================
# Ejecución de las pruebas
# ==========================================
if __name__ == '__main__':
    # Se añade verbosity=2 para tener un reporte detallado en la consola
    unittest.main(verbosity=2)