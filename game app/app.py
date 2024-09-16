from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

# Create a Flask app instance
app = Flask(__name__)

# Set a secret key for flash messages (used to show alerts to the user)
app.secret_key = "supersecretkey"

# Function to connect to the SQLite database
def get_db_connection():
    # Connect to 'games.db' database - or whatever you have called it
    conn = sqlite3.connect('games.db')
    # This makes it easier to access rows as dictionaries and the
    # data by the field heading rather than numbers
    conn.row_factory = sqlite3.Row
    return conn

# Route for the home page ('/') - when the user visits the home page, this function runs
@app.route('/')
def index():
    # Render the 'index.html' template and display is in the browser
    return render_template('index.html')

# Route to view all games
@app.route('/games')
def view_games():
    # Render the 'view_games.html' template and display it in the browser
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM games")
    games = cursor.fetchall()
    conn.close()
    return render_template('view_games.html', games=games)

# Route to add a new game to the databse ('/add') - handles both GET
# (show the form) and POST (submit the form)
@app.route('/add', methods=('GET', 'POST'))
def add_game():
    # If the form was submitted (POST request)
    if request.method == 'POST':
        # Get form data: title, platform, genre, year, sales
        title = request.form['title']
        platform = request.form['platform']
        genre = request.form['genre']
        year = request.form['year']
        sales = request.form['sales']
        
        # If any field is missing, show an error message
        if not title or not platform or not genre or not year or not sales:
            flash('All fields are required!')
        else:
            # If everything is filled in, insert the new game into the 
            # database
            conn = get_db_connection()
            conn.execute('INSERT INTO games (title, platform, genre, year, sales) VALUES (?, ?, ?, ?, ?)',
                        (title, platform, genre, year, sales))
        # Save the changes to the database
        conn.commit()
        # Close the connection
        conn.close()
        #Redirect to the 'view_games' page
        return redirect(url_for('view_games'))
    # If it's a GET request (the user is just visiting the page),
    # show the form to add a new game
    return render_template('add_games.html')

# Route to edit an existing game ('/edit/<int:id>')
# - allows users to update game data
@app.route('/edit/<int:id>', methods=('GET', 'POST'))
def edit_game(id):
    # Connect to the database and get the game with the given id
    conn = get_db_connection()
    game = conn.execute('SELECT * FROM games WHERE id = ?', (id,)).fetchone()
    
    # If the form was submitted (POST request)
    if request.method == 'POST':
        # Get the updated data from the form
        title = request.form['title']
        platform = request.form['platform']
        genre = request.form['genre']
        year = request.form['year']
        sales = request.form['sales']
        
        # If any field is missing, show an error message
        if not title or not platform or not genre or not year or not sales:
            flash('All field are required!')
        else:
            # Update the game in the database with the new data
            conn.execute('UPDATE games SET title = ?, platform = ?, genre = ?, year = ?, sales = ? WHERE id = ?',
                         (title, platform, genre, year, sales, id))
            # Save the changes to the database
            conn.commit()
            # Close the connection
            conn.close()
            #Redirect to the 'view_games' page
            return redirect(url_for('view_games'))      
    # If it's a GET request, show the form with the existing
    # game data so the user can edit it
    return render_template('edit_game.html', game=game)      

# Run the Flas app in debug mode (so we can see errors easily while developing)
if __name__ == '__main__':
    app.run(debug=True)