from search_def import *

def main_menu():
    search_type=[
        ["1. by title","2. by year","3. by gerne"],
        ["4. by actor","5. by years (from... to...)","6. by gerne and years"]
    ]
    search_static=["7. Show popular searches list","8. List of last searches"]
    print("\b\t***    WELCOME TO US   ***\n\t\tMake your choice!\n")
    print(f"{'SEARCH':<28}|{'SEARCH':<28}|{'SEARCH':<28}")
    print("_"*84)
    for type in search_type:
        print(f"{type[0]:<28}|{type[1]:<28}|{type[2]:<26}")
    print("_" * 84)
##проваливаться
    print(f"Statistic:      {search_static[0]:<40} {search_static[1]:<40}")
    print("_" * 84)
    print(f"{"9. Go out":>25}")
    print("_" * 84)
    while True:
        try:
            user_choice=int(input("YOUR choice: "))
            if user_choice not in range(1,9):
                print("Please choice between 1 and 9.")
                continue
            return user_choice
        except ValueError:
            print("Please choice a number between 1 and 9.")

def main():
    while True:
        number_user_choice=main_menu()
        if number_user_choice==1:
            search_film_name()
        if number_user_choice==2:
            search_film_year()
        if number_user_choice==3:
            search_film_gerne()
        if number_user_choice==4:
            search_film_actor()
        if number_user_choice==5:
            search_film_years_range()
        if number_user_choice==6:
            search_film_gerne_and_years()
        if number_user_choice==7:
            show_popular_searches()
        if number_user_choice==8:
            show_last_searches()
        if number_user_choice==9:
            print("   GOODBEY!\n See you soon.")
            break

if __name__ == "__main__":
    main()
