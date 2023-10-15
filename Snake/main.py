from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snakey-Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score_keeper = Scoreboard()

screen.listen()
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

#  scoreboard
score_keeper.update_scoreboard()

is_running = True
while is_running:
    screen.update()
    time.sleep(.1)
    snake.move()



#  detect collision with food

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_keeper.increase_score()


#  detect collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        print("You crashed into the wall")
        score_keeper.reset()
        snake.reset()
#  detect collision with tail
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            score_keeper.reset()
            snake.reset()

screen.exitonclick()
