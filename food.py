from turtle import Turtle
import random

colors = ['white', 'green', 'yellow', 'red', 'blue']
shapes = ['square', 'circle', 'triangle', 'turtle']

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.new()

    def move(self):
        self.goto(self.xcor(), self.ycor() - 20)

    def new(self):
        self.shape(random.choice(shapes))
        self.color(random.choice(colors))
        num = random.uniform(0.5, 2)
        self.shapesize(num , num)
        self.goto(random.randint(-380, 380), 270)
