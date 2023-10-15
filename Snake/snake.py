from turtle import Turtle
start_position = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in start_position:
            self.add_segment(position)

    def add_segment(self, position):
        new_piece = Turtle("square")
        new_piece.color("white")
        new_piece.penup()
        new_piece.goto(position)
        self.snake_body.append(new_piece)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def reset(self):
        for seg in self.snake_body:
            seg.goto(1000,1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    def move(self):
        for piece in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[piece - 1].xcor()
            new_y = self.snake_body[piece - 1].ycor()
            self.snake_body[piece].goto(new_x, new_y)
        self.head.forward(20)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

