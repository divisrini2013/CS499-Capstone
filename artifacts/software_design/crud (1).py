from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure

class AnimalShelter:
    def __init__(self, username, password):
        HOST = "nv-desktop-services.apporto.com"
        PORT = 34540
        DB_NAME = "aac"  # database name from your setup
        COLLECTION_NAME = "animals"  # collection name from my import

        # Use authSource=aac since user created in 'aac' db
        self.uri = f"mongodb://aacuser:aacuser123@nv-desktop-services.apporto.com:34540/aac?authSource=aac"


        try:
            self.client = MongoClient(self.uri)
            self.database = self.client[DB_NAME]
            self.collection = self.database[COLLECTION_NAME]
            # Test connection and authentication
            self.client.admin.command('ping')
            print("Connected to MongoDB successfully.")
        except ConnectionFailure as e:
            print(f"Connection failure: {e}")
        except OperationFailure as e:
            print(f"Authentication failed: {e}")

    def create(self, data):
        if data and isinstance(data, dict):
            result = self.collection.insert_one(data)
            return str(result.inserted_id)
        else:
            raise ValueError("Data must be a dictionary.")

    def read(self, query):
        if query and isinstance(query, dict):
            results = self.collection.find(query)
            return list(results)
        else:
            raise ValueError("Query must be a dictionary.")

    def update(self, query, update_values):
        if query and isinstance(query, dict) and update_values and isinstance(update_values, dict):
            result = self.collection.update_many(query, {'$set': update_values})
            return result.modified_count
        else:
            raise ValueError("Query and update_values must be dictionaries.")

    def delete(self, query):
        if query and isinstance(query, dict):
            result = self.collection.delete_many(query)
            return result.deleted_count
        else:
            raise ValueError("Query must be a dictionary.")
