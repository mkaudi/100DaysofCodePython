from turtle import Screen, Turtle
import time

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake_segments = []
        self.start()
        self.head = self.snake_segments[0]


    def start(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        return self.snake_segments

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake_segments.append(new_segment)

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())

    def reset(self):
        for segment in self.snake_segments:
            segment.goto(1000, 1000)
        self.snake_segments.clear()
        self.start()
        self.head = self.snake_segments[0]

    def move(self):
       for seg in range(len(self.snake_segments) - 1, 0, -1):
                new_x = self.snake_segments[seg - 1].xcor()
                new_y = self.snake_segments[seg - 1].ycor()
                self.snake_segments[seg].goto(new_x, new_y)
       self.snake_segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.snake_segments[0].setheading(UP)

    def down(self):
        # for seg in range(len(self.snake_segments) - 1, 0, -1):
        #     new_x = self.snake_segments[seg - 1].xcor()
        #     new_y = self.snake_segments[seg - 1].ycor()
        #     self.snake_segments[seg].goto(new_x, new_y)
        if self.head.heading() != UP:
            self.snake_segments[0].setheading(DOWN)

    def left(self):
        # for seg in range(len(self.snake_segments) - 1, 0, -1):
        #     new_x = self.snake_segments[seg - 1].xcor()
        #     new_y = self.snake_segments[seg - 1].ycor()
        #     self.snake_segments[seg].goto(new_x, new_y)
        if self.head.heading() != RIGHT:
            self.snake_segments[0].setheading(LEFT)

    def right(self):
        # for seg in range(len(self.snake_segments) - 1, 0, -1):
        #     new_x = self.snake_segments[seg - 1].xcor()
        #     new_y = self.snake_segments[seg - 1].ycor()
        #     self.snake_segments[seg].goto(new_x, new_y)
        if self.head.heading() != LEFT:
            self.snake_segments[0].setheading(RIGHT)