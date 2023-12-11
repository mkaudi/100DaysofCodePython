from turtle import Turtle

class Game(Turtle):

    def __init__(self):
        super().__init__()



    def show_state_on_board(self, self.state, x, y):
        self.state.hideturtle()
        self.state.penup()
        self.the_state.goto(x, y)
        self.the_state.pendown()
        self.the_state.write(row.state)
        self.the_state.penup()

