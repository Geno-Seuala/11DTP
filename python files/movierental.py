movies = ["Up", "Big Hero 6", "Frozen", "Coco", 
"Moana", "Inside Out", "Monsters Inc."]

inventory = []

returned = []

def menu():
    while True:
        try:
            select = int(input("""
        Select one of the following:
        1: To Add a Movie
        2: To Search the available Movies
        3: To Rent a Movie
        4: To Return a Movie
        5: To Print a Report

"""))
            break
        except ValueError:
            print("Only enter numbers 1 to 5")
    return select

def add():
    print("Add was selected")
    movie = input("""
    Please enter the name of the movie that you wish to add:
    """)
    movies.append(movie)


def search():
    print("Search was selected")
    movie = input("""
    Please enter the name of the movie that
    you wish to search for.:
    """)    
    if movie in movies:
        print(movie, "is available to rent!")
    elif movie in inventory:
        print(movie, "is already in inventory")
    else:
        print(movie, "is not offered by us")

def rent():
    print("Rent was selected")
    movie = input("""
    Please enter the name of the movie that
    you wish to rent:
    """)    
    if movie in movies:
        inventory.append(movie)
        movies.remove(movie)
        print(movie, "Added to order.")
    else:
        print(movie, "Is not our movie list.")

def return_movie():
    print("Return Movie was selected")
    movie = input("""
    Please enter the title of the move that you
    wish to return: 
    """)
    if movie in inventory:
        inventory.remove(movie)
        movies.append(movie)
        returned.append(movie)

def report():
    print("Report was selected")
    print("Returned movies:", returned)
    print("Inventory:", inventory)
    print("Movies we have:", movies)


def main():
    while True:
        selected = menu()
        if selected == 1:
            add()
        elif selected == 2:
            search()
        elif selected == 3:
            rent()
        elif selected == 4:
            return_movie()
        elif selected == 5:
            report()
        else:
            print("Only select numbers 1 to 5")

main()