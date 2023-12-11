from flask import Flask

app = Flask(__name__)


def make_bold(word):
    def bolding():
        print(f"<b>{word}</b>")
    return bolding

@app.route('/')
def hello_world():
    return "Hello, World"

@app.route("/bye")
@make_bold
#@make_emphasis
#@make_underlined
def bye():
    return "Bye!"

@app.route("/<name>")
def greet(name):
    return f"Hello {name}!"

if __name__ == "__main__":
    app.run(debug=True)