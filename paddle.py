from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(1, 5)
        self.goto(0 ,-250)

    def go_right(self):
        if (self.xcor() <= 350):
            self.goto(self.xcor() + 40, self.ycor()) 

    def go_left(self):
        if (self.xcor() >= -350):
            self.goto(self.xcor() - 40, self.ycor()) 