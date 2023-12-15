import unittest
from app import create_app, db
from app.models import Data

class TestApp(unittest.TestCase):

    def setUp(self):
        # Configuración inicial para cada test
        self.app = create_app('development')  # Crea una instancia de la aplicación Flask en entorno de desarrollo
        self.client = self.app.test_client  # Crea un cliente para realizar solicitudes HTTP a la aplicación
        self.app_context = self.app.app_context()  # Crea un contexto de aplicación para realizar pruebas
        self.app_context.push()  # Activa el contexto de la aplicación
        db.create_all()  # Crea todas las tablas en la base de datos

    def tearDown(self):
        # Acciones posteriores a la ejecución de cada test
        db.session.remove()  # Elimina la sesión de la base de datos
        db.drop_all()  # Elimina todas las tablas de la base de datos
        self.app_context.pop()  # Desactiva el contexto de la aplicación

    def test_insert_data(self):
        # Prueba para la inserción de datos
        response = self.client().post('/data', json={"name": "Test Data"})  # Realiza una solicitud POST a /data
        self.assertEqual(response.status_code, 200)  # Verifica si el código de estado de la respuesta es 200 (OK)
        self.assertEqual(Data.query.count(), 1)  # Verifica si se ha insertado un dato en la base de datos

    def test_get_all_data(self):
        # Prueba para obtener todos los datos
        data = Data(name="Test Data")
        db.session.add(data)
        db.session.commit()
        
        response = self.client().get('/data')  # Realiza una solicitud GET a /data
        self.assertEqual(response.status_code, 200)  # Verifica si el código de estado de la respuesta es 200 (OK)
        self.assertEqual(len(response.json), 1)  # Verifica si se obtiene una lista con un elemento

    def test_delete_data(self):
        # Prueba para eliminar datos
        data = Data(name="Test Data")
        db.session.add(data)
        db.session.commit()

        response = self.client().delete(f'/data/{data.id}')  # Realiza una solicitud DELETE a /data/id
        self.assertEqual(response.status_code, 200)  # Verifica si el código de estado de la respuesta es 200 (OK)
        self.assertEqual(Data.query.count(), 0)  # Verifica si no hay datos en la base de datos después de la eliminación


if __name__ == '__main__':
    unittest.main()  # Ejecuta los tests si el archivo es ejecutado directamente

