from turtle import *
from snake import Snake
from food import Food
from ScoreBoard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detecting collision with food using the method "distance"
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()


    # detect collision with wall

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on=False
        scoreboard.gameover()

    # for collision with head
    for segment in snake.segments[1:]:  # also called slicing  in this the range is set such that every segment of snake is included except 1: which is the head of the snake
        if snake.head.distance(segment) < 10:
            game_is_on= False
            scoreboard.gameover()



screen.exitonclick()