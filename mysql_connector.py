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

    def get_genres(self):
        query = """
        Select distinct c.name
        from category as c
        join film_category as fc
        on c.category_id=fc.category_id
        """
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            return [row["name"] for row in cursor.fetchall()]

    def get_years_by_genre(self, genre):
        query = """
                Select MIN(f.release_year) as year_from, MAX(f.release_year) as year_to
                from film as f
                join film_category as fc
                on f.film_id=fc.film_id
                join category as c
                on fc.category_id=c.category_id
                where c.name=%s
                
                """
        with self.connection.cursor() as cursor:
            cursor.execute(query, (genre,))
            return cursor.fetchall()



    def search_film_name(self, name, offset=0, limit=10):
        query="""
        SELECT title, release_year
        FROM film
        Where title like %s
        LIMIT %s OFFSET %s
        """
        with self.connection.cursor() as cursor:
            cursor.execute(query, (f"%{name.lower()}%", limit,offset))
            return cursor.fetchall()

    def search_film_year(self, year):
        query="""
        SELECT title, release_year
        FROM film
        Where release_year = %s
        """
        with self.connection.cursor() as cursor:
            cursor.execute(query, (year,))
            return cursor.fetchall()

    def search_film_gerne(self, genre):
        query="""
        SELECT f.title, f.release_year, c.name as genre
        FROM film as f
        JOIN film_category as fc
        ON f.film_id=fc.film_id
        JOIN category as c
        ON fc.category_id=c.category_id
        Where c.name like %s
        """
        with self.connection.cursor() as cursor:
            cursor.execute(query,(f"%{genre}%",))
            return cursor.fetchall()

    def search_film_actor(self, actor_name):
        query = """
         SELECT f.title, f.release_year, CONCAT(a.first_name," ",a.last_name) as actor_name
         FROM film as f
         JOIN film_actor as fa
         ON f.film_id=fa.film_id
         JOIN actor as a
         ON fa.actor_id=a.actor_id
         Where LOWER(CONCAT(a.first_name," ",a.last_name)) like %s
         """
        with self.connection.cursor() as cursor:
            cursor.execute(query, (f"%{actor_name}%",))
            return cursor.fetchall()

    def search_film_years(self, year_from, year_to):
        query = """
          SELECT title, release_year
          FROM film
          Where release_year BETWEEN %s AND %s
          """
        with self.connection.cursor() as cursor:
            cursor.execute(query, (year_from, year_to))
            return cursor.fetchall()

    def search_film_gerne_and_years(self, genre,year_from, year_to):
        query = """
          SELECT f.title, f.release_year, c.name as genre
          FROM film as f
          JOIN film_category as fc
        ON f.film_id=fc.film_id
        JOIN category as c
        ON fc.category_id=c.category_id
        Where c.name like %s AND f.release_year BETWEEN %s AND %s
        """
        with self.connection.cursor() as cursor:
            cursor.execute(query, (f"%{genre}%",year_from, year_to))
            return cursor.fetchall()

    def get_genres_with_years(self):
        query = """
                  Select distinct c.name as genre, MIN(f.release_year) as year_from, MAX(f.release_year) as year_to
        from film as f 
        join film_category as fc
        on f.film_id=fc.film_id
        join category as c
        on c.category_id=fc.category_id
        group by c.name
        order by c.name
                """
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()



