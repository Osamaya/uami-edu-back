from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

# Cargar las variables del archivo .env
load_dotenv()
load_dotenv(override=True)
 
class MongoDBConnection:
    def __init__(self, uri: str):
        db_name = os.getenv("MONGO_DB")
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        self.db = self.client[db_name]  # Cambia 'nombre_base_datos' por tu base de datos

    def get_collection(self, collection_name: str):
        return self.db[collection_name]

# Singleton para una única conexión en la aplicación
def get_db_connection():
    db_uri = os.getenv("MONGO_URI")
    return MongoDBConnection(db_uri)
