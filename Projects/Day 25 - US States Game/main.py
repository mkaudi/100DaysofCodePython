import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

states = pd.read_csv("50_states.csv")

guessed_states = []
score = 0
# keep playing the game
while len(guessed_states) < 50:
    # create the prompt box and capitalize the answer that you get
    answer_state = screen.textinput(title=f"{score}/50 Guess the state", prompt="What's another state's name?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        break
    # go through the states and see if the user provided answer is correct,
    # if so write the answer onto the location of the state on the map
    else:
        for index, row in states.iterrows():
            if row.state == answer_state:
                the_state = turtle.Turtle()
                the_state.hideturtle()
                the_state.penup()
                the_state.goto(row.x, row.y)
                the_state.pendown()
                the_state.write(row.state)
                the_state.penup()
                guessed_states.append(answer_state)
                score += 1
                break
# generate a file with states that the user didn't get
states_list = states.state.to_list()
diff = list(set(states_list) - set(guessed_states))
print(len(diff))
diff = pd.to_csv("States_to_learn.csv")


# turtle.mainloop()
