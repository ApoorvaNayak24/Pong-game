from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("blue")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

computer_paddle = Paddle((-350, 0))
player_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player_paddle.go_up, "Up")
screen.onkey(player_paddle.go_down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Computer paddle follows the ball
    computer_paddle.follow_ball(ball)

    #Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddles
    if (ball.distance(computer_paddle) < 50 and ball.xcor() < -340) or (ball.distance(player_paddle) < 50 and ball.xcor() > 340):
        ball.bounce_x()

    #Detect if the ball goes out of bounds
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
