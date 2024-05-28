from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def follow_ball(self, ball):
        if self.ycor() < ball.ycor() and abs(self.ycor() - ball.ycor()) > 10:
            self.go_up()
        elif self.ycor() > ball.ycor() and abs(self.ycor() - ball.ycor()) > 10:
            self.go_down()
