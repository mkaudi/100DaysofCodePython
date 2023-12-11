from flask import Flask
from random import *

app = Flask(__name__)

random_num = randint(0, 10)

@app.route('/')
def guess_number():
    return ("<h1>Guess a number between 0 and 9</h1>"
          "<img src= https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>")

@app.route('/<int:num>')
def chosen_number(num):
    if num == random_num:
        return f"<h1>You found me</h1>" \
               f"<img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif>"
    elif num < random_num:
        return f"<h1>Too low, try again</h1>" \
               f"<img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>"
    else:
        return f"<h1>Too high, try again</h1>" \
               f"<img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>"


if __name__ == "__main__":
    app.run()
