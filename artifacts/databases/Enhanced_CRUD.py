import os
import logging
from pymongo import MongoClient, ASCENDING
from pymongo.errors import ConnectionFailure, OperationFailure, PyMongoError
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(
    filename="database_operations.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class AnimalShelter:
    

    def __init__(self):

        # Load configuration
        self.username = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASS")
        self.host = os.getenv("DB_HOST")
        self.port = os.getenv("DB_PORT")
        self.db_name = os.getenv("DB_NAME")
        self.collection_name = os.getenv("DB_COLLECTION")

        # Build secure MongoDB URI
        self.uri = f"mongodb://{self.username}:{self.password}@{self.host}:{self.port}/{self.db_name}?authSource={self.db_name}"

        try:
            self.client = MongoClient(self.uri, serverSelectionTimeoutMS=5000)
            self.database = self.client[self.db_name]
            self.collection = self.database[self.collection_name]

            # Verify connection
            self.client.admin.command("ping")
            logging.info("Successfully connected to MongoDB.")
            print("Database connection established.")

            # Ensure indexes for performance
            self.collection.create_index([("name", ASCENDING)])
            self.collection.create_index([("animal_type", ASCENDING)])
            logging.info("Indexes ensured on: name, animal_type")

        except ConnectionFailure as e:
            logging.error(f"Connection failure: {str(e)}")
            raise ConnectionFailure("MongoDB is not reachable. Check server settings.")
        except OperationFailure as e:
            logging.error(f"Authentication failed: {str(e)}")
            raise OperationFailure("Invalid database credentials.")
        except Exception as e:
            logging.error(f"Unexpected error during initialization: {str(e)}")
            raise

    def validate_dict(self, data):
        """
        Validate that the provided input is a non-empty dictionary.
        """
        if not isinstance(data, dict):
            raise TypeError("Input must be a dictionary.")
        if len(data) == 0:
            raise ValueError("Dictionary cannot be empty.")
        return True

    def create(self, data):
        """
        Create a document in the animals collection.
        """
        try:
            self.validate_dict(data)
            result = self.collection.insert_one(data)
            logging.info(f"Inserted document with ID: {result.inserted_id}")
            return str(result.inserted_id)
        except PyMongoError as e:
            logging.error(f"Database insertion error: {str(e)}")
            return None

    def read(self, query):
        """
        Retrieve documents based on a MongoDB query.
        """
        try:
            self.validate_dict(query)
            results = list(self.collection.find(query))
            logging.info(f"Read operation returned {len(results)} documents.")
            return results
        except PyMongoError as e:
            logging.error(f"Database read error: {str(e)}")
            return []

    def update(self, query, update_values):
        """
        Update documents matching the query with given fields.
        """
        try:
            self.validate_dict(query)
            self.validate_dict(update_values)

            result = self.collection.update_many(query, {"$set": update_values})
            logging.info(f"Updated {result.modified_count} documents.")
            return result.modified_count
        except PyMongoError as e:
            logging.error(f"Database update error: {str(e)}")
            return 0

    def delete(self, query):
        """
        Delete documents based on a query.
        """
        try:
            self.validate_dict(query)
            result = self.collection.delete_many(query)
            logging.info(f"Deleted {result.deleted_count} documents.")
            return result.deleted_count
        except PyMongoError as e:
            logging.error(f"Database delete error: {str(e)}")
            return 0
