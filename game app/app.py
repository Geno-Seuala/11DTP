from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

# Create a Flask app instance
app = Flask(__name__)


# Route for the home page ('/') - when the user visits the home page, this function runs
@app.route('/')
def index():
    # Render the 'index.html' template and display is in the browser
    return render_template('index.html')

# Route to view all games
@app.route('/games')
def view_games():
    # Render the 'view_games.html' template and display it in the browser
    return render_template('view_games.html')

# Route to add a new game
@app.route('/add')
def add_game():
    # Render the 'add_games.html' template and display it in the browser
    return render_template('add_games.html')

# Run the Flas app in debug mode (so we can see errors easily while developing)
if __name__ == '__main__':
    app.run(debug=True)