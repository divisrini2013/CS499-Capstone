"""
Enhanced AnimalShelter CRUD Module for CS 499 Capstone
Author: Divya Rangaraj
Description:
    This module provides a secure, maintainable, and production-ready version 
    of the AnimalShelter data access layer. Enhancements include:
    - Secure environment-based configuration
    - Structured logging
    - Robust input validation
    - Exception handling with error propagation
    - Modular design principles
"""

import os
import logging
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure, ConfigurationError

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    filename='animal_shelter.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

class AnimalShelter:
    """
    A secure and maintainable CRUD interface for the AAC Animal Shelter database.
    """

    def __init__(self):
        """Initialize database connection using secure environment variables."""

        try:
            self.user = os.getenv("DB_USER")
            self.password = os.getenv("DB_PASS")
            self.host = os.getenv("DB_HOST")
            self.port = os.getenv("DB_PORT")
            self.db_name = os.getenv("DB_NAME")
            self.collection_name = os.getenv("DB_COLLECTION")

            if not all([self.user, self.password, self.host, self.port, self.db_name]):
                raise ConfigurationError("Missing one or more required environment variables")

            # Construct secure MongoDB URI
            uri = f"mongodb://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}?authSource={self.db_name}"

            # Connect to MongoDB
            self.client = MongoClient(uri, serverSelectionTimeoutMS=5000)
            self.database = self.client[self.db_name]
            self.collection = self.database[self.collection_name]

            # Test connection
            self.client.admin.command('ping')
            logging.info("Successfully connected to MongoDB.")

        except (ConnectionFailure, OperationFailure, ConfigurationError) as e:
            logging.error(f"Database initialization error: {e}")
            raise

    # -----------------------------------------------------------
    # CREATE
    # -----------------------------------------------------------
    def create(self, data: dict):
        """Insert a new document into the collection."""

        try:
            if not isinstance(data, dict) or not data:
                raise ValueError("Input data must be a non-empty dictionary.")

            result = self.collection.insert_one(data)
            logging.info(f"Inserted new document with _id {result.inserted_id}")
            return str(result.inserted_id)

        except Exception as e:
            logging.error(f"Error creating document: {e}")
            return None

    # -----------------------------------------------------------
    # READ
    # -----------------------------------------------------------
    def read(self, query: dict):
        """Retrieve documents matching a query."""

        try:
            if not isinstance(query, dict):
                raise ValueError("Query must be a dictionary.")

            results = self.collection.find(query)
            results_list = list(results)
            logging.info(f"Read operation returned {len(results_list)} records.")
            return results_list

        except Exception as e:
            logging.error(f"Error reading documents: {e}")
            return []

    # -----------------------------------------------------------
    # UPDATE
    # -----------------------------------------------------------
    def update(self, query: dict, update_values: dict):
        """Update documents that match a query."""

        try:
            if not isinstance(query, dict) or not isinstance(update_values, dict):
                raise TypeError("Query and update_values must be dictionaries.")
            if not query or not update_values:
                raise ValueError("Query and update_values cannot be empty.")

            result = self.collection.update_many(query, {"$set": update_values})
            logging.info(f"Updated {result.modified_count} document(s).")
            return result.modified_count

        except Exception as e:
            logging.error(f"Error updating documents: {e}")
            return 0

    # -----------------------------------------------------------
    # DELETE
    # -----------------------------------------------------------
    def delete(self, query: dict):
        """Delete documents that match a query."""

        try:
            if not isinstance(query, dict) or not query:
                raise ValueError("Query must be a non-empty dictionary.")

            result = self.collection.delete_many(query)
            logging.info(f"Deleted {result.deleted_count} document(s).")
            return result.deleted_count

        except Exception as e:
            logging.error(f"Error deleting documents: {e}")
            return 0
