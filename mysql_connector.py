import os
from os import environ
import pymysql
from pymysql.cursors import DictCursor
from dotenv import load_dotenv

load_dotenv()

# def get_connection_sql() ->pymysql.connections.Connection:
#     return pymysql.connect(
#         host=os.getenv("HOST"),
#         user=os.getenv("USER"),
#         password=os.getenv("PASSWORD"),
#         database=os.getenv("DATABASE"),
#         cursorclass=DictCursor,
#         autocommit=True,
#     )
MONGO_URI=os.getenv("MONGO_URI")
MONGO_DB_NAME=os.getenv("MONGO_DB_NAME")
MONGO_COLLECTION_NAME=os.getenv("MONGO_COLLECTION_NAME")

# if __name__ == "__main__":
#     print(f"HOST:", os.getenv("HOST"),"\nUSER:", os.getenv("USER"),
#     "\nDATABASE:", os.getenv("DATABASE"))

class DBConnector:
    def __init__(self):
        self.connection=pymysql.connect(
            host=os.getenv("HOST"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            database=os.getenv("DATABASE"),
            cursorclass=DictCursor,
            autocommit=True,
        )
        def close(self):
            if self.connection:
                self.connection.close()

        def search_film_name(self, name, offset=0, limit=10):
            query="""
            SELECT title, release_year
            FROM film
            Where title ilike %s
            LIMIT %s OFFSET %s
            """
            with self.connection.cursor() as cursor:
                cursor.execute(query, (f"%{name}%", limit,offset))
                return cursor.fetchall()