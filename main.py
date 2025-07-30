from search_def import *
import sys



def main_menu():
    search_type=[
        ["1. by title","2. by year","3. by genre"],
        ["4. by actor","5. by years (from... to...)","6. by genre and years"]
    ]

    print("\b\t***    WELCOME TO US   ***\n\t\tMake your choice!\n")
    print(f"{'SEARCH':<28}|{'SEARCH':<28}|{'SEARCH':<28}")
    print("_"*84)
    for type in search_type:
        print(f"{type[0]:<28}|{type[1]:<28}|{type[2]:<26}")
    print("_" * 84)
##проваливаться
    print(f"7. Show statistic")
    print("_" * 84)
    print(f"8. Go out")
    print("_" * 84)
    while True:
        try:
            user_choice=int(input("YOUR choice: "))
            if user_choice not in range(1,9):
                print("Please choice between 1 and 8.")
                continue
            return user_choice
        except ValueError:
            print("Please choice a number between 1 and 8.")

def stat_menu():
    search_static = ["1. Show popular searches list", "2. List of last searches"]
    print(f"\n\n\nMake your choice: ")
    print("_" * 84)
    print(f"SEARCH: {search_static[0]:<40} {search_static[1]:<40} ")
    print("_" * 84)
    print(f"{"3. Go to main menu":>26} {"4. Go out":>31}")
    print("_" * 84)
    while True:
        try:
            user_choice_st = int(input("YOUR choice: "))
            if user_choice_st not in range(1, 5):
                print("Please choice between 1 and 4.")
                continue
            return user_choice_st
        except ValueError:
            print("Please choice a number between 1 and 4.")



def main():
    while True:
        number_user_choice=main_menu()
        if number_user_choice==1:
            search_film_name()
        elif number_user_choice==2:
            search_film_year()
        elif number_user_choice==3:
            search_film_genre()
        elif number_user_choice==4:
            search_film_actor()
        elif number_user_choice==5:
            search_film_years_range()
        elif number_user_choice==6:
            search_film_genre_and_years()
        elif number_user_choice==7:
            while True:
                user_choice_st=stat_menu()
                if user_choice_st == 1:
                    show_popular_searches()
                elif user_choice_st == 2:
                    show_last_searches()
                elif user_choice_st==3:
                    break
                elif user_choice_st==4:
                    print("   GOODBEY!\n See you soon.")
                    exit()
        elif number_user_choice==8:
            print("   GOODBEY!\n See you soon.")
            exit()

if __name__ == "__main__":
    main()
