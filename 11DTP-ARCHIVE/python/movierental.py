movies = ["Up", "Big Hero 6", "Frozen", "Coco",
          "Moana", "Inside Out", "Monsters Inc."]

inventory = []

returned = []


def menu():
    """
    Prints a menu for the user to choose an operation
    Returns: select = integer
    """
    while True:
        try:
            select = int(input("""
        Select one of the following:
        1: To Add a Movie
        2: To Search the available Movies
        3: To Rent a Movie
        4: To Return a Movie
        5: To Print a Rental Report
        6: To Exit

"""))
            break
        except ValueError:
            print("Only enter numbers 1 to 5")
    return select


def add():
    """
    Adds a movie to the stores stock
    Returns: Change of list - movies
    """
    print("Add was selected")
    print("These are the movies we currently have:", movies)
    movie = input("""
    Please enter the name of the movie that you wish to add:
    """)
    movies.append(movie)
    print("Movies in stock:", movies)


def search():
    """
    Allows the user to search within the stores stock for a movie
    returns: info on movie (whether it is offered by us)
    """
    print("Search was selected")
    movie = input("""
    Please enter the name of the movie that
    you wish to search for.:
    """)
    if movie in movies:
        print(movie, "is available to rent!")
    elif movie in inventory:
        print(movie, "is already in cart")
    else:
        print(movie, "is not offered by us")


def rent():
    """
    Removes a movie from the stores stock and adds it into
    the users cart
    Returns: Removes movie from list - movies
    """
    print("Rent was selected")
    print("Here are the movies we have:", movies)
    movie = input("""
    Please enter the name of the movie that
    you wish to rent:
    """)
    if movie in movies:
        inventory.append(movie)
        movies.remove(movie)
        print(movie, "Added to cart.")
    else:
        print(movie, "Is not our movie list.")


def return_movie():
    """
    Removes a movie from the users cart and adds it into
    the stores stock
    Returns: updated list - movies
    """
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
    """
    Gives the user a full, in depth rental report
    Returns: the users cart, the stores stock, and the movies that
    the user had taken out and returned to the store
    
    """
    print("Report was selected")
    print("Returned movies:", returned)
    print("Cart:", inventory)
    print("Movies we have:", movies)


def main():
    """
    Calls any of the operations depending on what the user
    selects in menu()
    returns: selected = menu()
    """
    while True:
        try:
            selected = menu()
        except ValueError:
            print("Please only enter whole numbers")
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
        elif selected == 6:
            break
        else:
            print("Only select numbers 1 to 6")

# Runs the program


main()
