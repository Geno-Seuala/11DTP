from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to add a game
@app.route("/register")
def add_game():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)