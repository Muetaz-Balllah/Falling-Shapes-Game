from turtle import Turtle, Screen
from paddle import Paddle
from food import Food
from dashboard import Board
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Falling Shapes Game")
screen.tracer(0)

player = Paddle()
point = Food()
board = Board()

screen.listen()
screen.onkey(player.go_right, "Right")
screen.onkey(player.go_left, "Left")
screen.onkey(screen.exitonclick, 'p')

defult_time = 0.1

while True:
    screen.update()
    time.sleep(defult_time)
    point.move()

    if point.distance(player) < 50 and point.ycor() <= -250:
        if point.shape() == 'turtle' and point.color()[0] == 'white':
            break
        if point.shape() == 'turtle':
            board.update(5)
        elif point.shape() == 'square':
            board.update(2)
        elif point.shape() == 'circle':
            board.update(1)
        elif point.shape() == 'triangle':
            board.update(0)
            defult_time = 0.1

        defult_time *= 0.9
        point.new()

    if point.ycor() <= -300:
        point.new()
    

board.Game_over()
    
screen.exitonclick()
