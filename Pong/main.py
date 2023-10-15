from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

score_keeper = Scoreboard()
screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

game_ball = Ball((0, 0))
game_ball.move()


game_on = True
while game_on:
    BALL_SPEED = .1
    screen.update()
    time.sleep(BALL_SPEED)
    game_ball.move()

# Detects wall collisions
    if game_ball.ycor() > 280 or game_ball.ycor() < -280:
        game_ball.y_bounce()

# Detect paddle hits
    if r_paddle.distance(game_ball) < 50 and game_ball.xcor() > 320 or l_paddle.distance(game_ball) < 50 and game_ball.xcor() < -320:
        game_ball.x_bounce()
        BALL_SPEED += .1

# Detect right paddle misses
    if game_ball.xcor() > 380:
        game_ball.reset_ball()
        score_keeper.l_point()

# Detect left paddle misses
    if game_ball.xcor() < -380:
        game_ball.reset_ball()
        score_keeper.r_point()

    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")

    screen.listen()




screen.exitonclick()
