from turtle import Turtle

class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.point = -1
        self.goto(0, 250)
        self.update(1)

    def update(self, num):
        self.clear()
        if num != 0:
            self.point += num
        else:
            self.point = 0
        self.write(self.point, align='center', font=('courier', 30, 'normal'))


    def Game_over(self):
        self.goto(0, 0)
        self.write('Game Over', align='center', font=('courier', 50, 'normal'))