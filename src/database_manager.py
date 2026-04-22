"""Database Manager for E-commerce pipeline.
    Handles all connections and operations with MSSQL."""



import pyodbc
import os
from dotenv import load_dotenv

#Read .env file from the project root
#os.path.dirname gets the folder of THIS file (src/)
#os.path.join goes up one level (..) to find .env in the root 
dotenv_path = os.path.join(os.path.dirname(__file__),'..','.env')
load_dotenv(dotenv_path)

class DatabaseManager:
    """Manage Database connections and queries."""

    def __init__(self):
        """Load database config from .env file"""
        self.server = os.getenv("DB_SERVER")
        self.database = os.getenv("DB_NAME")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.driver = os.getenv("DB_DRIVER")
        self.connection = None

    def connect(self):
        """Open connection to the database."""
        try:
            conn_str = (
                f"DRIVER={{{self.driver}}};"
                f"SERVER={self.server};"
                f"DATABASE={self.database};"
                f"UID={self.user};"
                f"PWD={self.password};"
                "TrustServerCertificate=yes;"
            )
            self.connection = pyodbc.connect(conn_str)
            print(f"Connected to {self.database} successfully.")

        except pyodbc.Error as e:
            print(f"Connection failed: {e}")
            raise
        
    def execute_query(self, query, params=None):
        """Execute INSERT, UPDATE AND DELETE queries."""
        if self.connection is None:
            self.connect()

        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully.")

        except pyodbc.Error as e:
            self.connection.rollback()
            print(f"Query failed: {e}")
            raise
    
    def fetch_data(self, query, params=None):
        """Execute SELECT queries and return results."""
        if self.connection is None:
            self.connect()

        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            rows = cursor.fetchall()
            return rows
        
        except pyodbc.Error as e:
            print(f"Fetch failed: {e}")
            raise



    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            self.connection = None
            print("Connection closed.")

        else:
            print("No active connection to close.")
        
   


