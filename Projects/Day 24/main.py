from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

new_snake = Snake()
food = Food()
scoreboard = ScoreBoard()
snake = new_snake.start()

screen.listen()
screen.onkey(new_snake.up, "Up")
screen.onkey(new_snake.down,"Down")
screen.onkey(new_snake.left,"Left")
screen.onkey(new_snake.right,"Right")


scoreboard.show_score()
yes_no = True
while yes_no:
    screen.update()
    time.sleep(0.1)
    new_snake.move()

    #detect collission
    if new_snake.head.distance(food) < 15:
        food.refresh()
        new_snake.extend()
        scoreboard.increase_score()

    #Detect collission with wall
    if new_snake.head.xcor() > 288 or new_snake.head.xcor() < -288 or new_snake.head.ycor() > 288 or new_snake.head.ycor() < -288:
        scoreboard.reset()
        new_snake.reset()


    #detect collision with tail
    for segment in new_snake.snake_segments[1:]:
        if new_snake.head.distance(segment) < 10:
            scoreboard.reset()
            new_snake.reset()







#
# starting_pos = [(0,0), (-20,0), (-40,0)]
#
# segments = []
#
# for position in starting_pos:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)
# run = True
#
# while run:
#     screen.update()
#     time.sleep(0.1)
#     for seg in range(len(segments)-1, 0,-1):
#         new_x = segments[seg - 1].xcor()
#         new_y = segments[seg -1].ycor()
#         segments[seg].goto(new_x,new_y)
#     segments[0].forward(20)
#
#
#
#
#


# snake1 = Turtle()
# snake2 = Turtle()
# snake3 = Turtle()
#
# snake1.color("white")
# snake2.color("white")
# snake3.color("white")
#
# snake1.shape("square")
# snake2.shape("square")
# snake3.shape("square")

# snake2.goto(-20,0)
# snake3.goto(-40,0)

screen.exitonclick()
