# from config.conn import get_db_connection
from app.db.mongo.conn import get_db_connection
from pymongo.results import InsertOneResult, UpdateResult,DeleteResult
from typing import Dict, Optional, Any, Union, List

class Report:
    def __init__(self, collection_name: str):
        self.db_connection = get_db_connection()
        self.collection_name = collection_name  # Guardamos el nombre
        self.collection = self.db_connection.get_collection(collection_name)
    # La proyección en MongoDB es como un "select" de campos específicos que quieres recuperar de los documentos, similar a SELECT campo1, campo2 en SQL.
    def find(self, query: Dict = {}, projection: Optional[Dict] = None) -> List[Dict]:
        # Usamos el método `find` de la colección para obtener múltiples documentos
        return list(self.collection.find(query,projection))
    
    def find_one(self, query: Dict, projection: Optional[Dict] = None) -> Optional[Dict]:
        """Busca un único documento con opción de proyección"""
        return self.collection.find_one(query, projection)

    def insert_one(self, document: Dict) -> InsertOneResult:
        """Inserta un nuevo documento"""
        return self.collection.insert_one(document)
    # Upsert: es una combinación de "update" + "insert". Si el documento existe, lo actualiza; si no existe, lo crea. Esto nos hace evitar una validacion de si existe lo actualizo y si no lo creo.
    def update_one(
        self, 
        query: Dict, 
        update: Dict, 
        upsert: bool = False,
        array_filters: Optional[List[Dict]] = None
    ) -> UpdateResult:
        """
        Actualiza un documento con opción a upsert y array_filters
        """
        return self.collection.update_one(
            query, 
            update, 
            upsert=upsert,
            array_filters=array_filters
        )

    def update_many(
        self,
        query: Dict,
        update: Dict,
        upsert: bool = False
    ) -> UpdateResult:
        """Actualiza múltiples documentos"""
        return self.collection.update_many(query, update, upsert=upsert)

    def replace_one(
        self,
        query: Dict,
        replacement: Dict,
        upsert: bool = False
    ) -> UpdateResult:
        """Reemplaza completamente un documento"""
        return self.collection.replace_one(query, replacement, upsert=upsert)

    def delete_one(self, query: Dict) -> DeleteResult:
        """Elimina un documento"""
        return self.collection.delete_one(query)

    def delete_many(self, query: Dict) -> DeleteResult:
        """Elimina múltiples documentos"""
        return self.collection.delete_many(query)

    def aggregate(self, pipeline: List[Dict]) -> List[Dict]:
        """Ejecuta una pipeline de agregación"""
        return list(self.collection.aggregate(pipeline))

    def count_documents(self, query: Dict) -> int:
        """Cuenta documentos que coinciden con la query"""
        return self.collection.count_documents(query)

    def bulk_write(self, operations: List) -> Any:
        """Ejecuta operaciones en lote"""
        return self.collection.bulk_write(operations)