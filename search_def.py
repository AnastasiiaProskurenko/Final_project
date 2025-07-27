from operator import index

from mysql_connector import DBConnector
from log_writer import search_write
from log_stats import *
from formatter import *
from gerne_menu import *


db=DBConnector()
logger = search_write()
statistic=LogStats(logger)



def search_film_name():
    name = input("Enter movie title: ")
    results = db.search_film_name(name)
    logger.log_search("by title", {"title": name}, len(results))
    paginate_results(results, ["title", "release_year"])

def search_film_year():
    while True:
        user_inp = int(input("Enter release year(from 1990): "))
        if user_inp == "0":
            return
        try:
            year=int(user_inp)
            if year<1990:
                print("Invalid year, must be 1990 or later.")
                continue
        except ValueError:
            print("Invalid year format.")
            continue
        break
    results = db.search_film_year(year)
    logger.log_search("by year", {"year":year}, len(results))
    paginate_results(results, ["title", "release_year"])


def search_film_gerne():
    genres=db.get_genres()
    print_table([{"#": i+1, "Genre": g} for i, g in enumerate(genres)], ["#","Genre" ])
    try:
        index=int(input("Choose genre number: "))-1
        if index not in range(len(genres)):
            print("Invalid selection.")
            return
        genre=genres[index]
        results=db.search_film_gerne(genre)
        logger.log_search("by gerne", {"gerne": genre}, len(results))
        paginate_results(results, ["title", "release_year"])
    except ValueError:
        print("Invalid input.")

def search_film_actor():
    while True:
        actor=input("Enter actor name(or 0 to return to main menu): ").strip().lower()
        if actor=="0":
            return
        if not actor:
            print("Actor name cannot be empty. Try again.")
            continue
        results=db.search_film_actor(actor)
        if not results:
            print(f"No films found for actor {actor.title()}. Try again or enter 0 to return to main menu.")
            continue
        logger.log_search("by actor", {"actor": actor.title()}, len(results))
        paginate_results(results, ["title", "release_year", "actor_name"])
        break

def search_film_years_range():
    while True:
        try:
            year_from= int(input("From year: "))
            year_to=int(input("To year: "))
            if year_from<1990 or year_to<1990:
                print("Invalid year, must be 1990 and greate.")
                continue
            if year_from > year_to:
                print("Error: 'From year' cannot be greater than 'To year'.")
                continue
            break
        except ValueError:
            print("Invalid year format.")
            return

    results=db.search_film_years(year_from,year_to)
    logger.log_search("by year", {"from":year_from,"to":year_to}, len(results))
    paginate_results(results, ["title", "release_year"])

def search_film_gerne_and_years():
    genres = db.get_genres_with_years()
    print("     Genre       |  Years")
    print("-"*84)
    for i, genre in enumerate(genres,1):
        print(f"{i:2} | {genre['genre']:<11} | {genre['year_from']} - {genre['year_to']}")
    try:
        index=int(input("Choice genre number: "))-1
        if  not (0<=index<len(genres)):
            print("Invalid genre selection.")
            return
        genre=genres[index]["genre"]
    except ValueError:
        print("Invalid input.")
        return

    while True:
        try:
            year_from = int(input("From year: "))
            year_to = int(input("To year: "))
            if not year_from or not year_to:
                print(f"No years found.")
                continue
            if year_from < 1990 or year_to < 1990:
                print("Invalid year, must be 1990 and greate.")
                continue
            if year_from>year_to:
                print("Start year must be less than or equal to end year.")
                continue
            break
        except ValueError:
            print("Invalid year format.Please try again.")

    results = db.search_film_gerne_and_years(genre,year_from, year_to)
    logger.log_search("by genre and years ", f"{genre}-{year_from}-{year_to}", len(results))
    paginate_results(results, ["title", "release_year"])


def show_popular_searches():
    print("\nTOP 5 most popular searches: \n")
    popular=statistic.get_popular()
    print_table(popular,["search_type","params", "count"])

def show_last_searches():
    print("\nLast 5 unique searches: \n")
    latest = statistic.get_latest()
    print_table(latest, ["search_type","params", "count"])
