from pymongo import MongoClient, errors
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI_ATLAS")
DB_NAME_ATLAS = os.getenv("MONGODB_DATA")

try:
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME_ATLAS]
    print("Conexión exitosa a Atlas")
    collections = db.list_collection_names()
    print("Conectado a MONGO DB Atlas: Base de Datos:", DB_NAME_ATLAS)
    print('Colecciones: ', (collections))

except errors.ServerSelectionTimeoutError as ex:
    print("No se pudo conectar al servidor", ex )
except errors.ConnectionFailure as ex:
    print("Falló la conexión a la base de datos")
except Exception as ex:
    print("Ocurrió un error inesperado:", ex)