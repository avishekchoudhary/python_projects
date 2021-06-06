from snake import Snake
from turtle import Screen
import time
from food import Food
from scoreboard import Score


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snakee')
screen.tracer(0)
 
snake = Snake()
bait = Food()
point = Score()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey( snake.right, 'Right')
screen.onkey(snake.left, 'Left')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.segments[0].distance(bait) < 15:
        bait.food_refresh()
        point.score_increase()
        snake.extend()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        snake.snake_reset()
        point.score_reset()
    
    for segment in snake.segments[1:]:
        if segment.distance(snake.segments[0]) < 10:
            snake.snake_reset()
            point.score_reset()
        

screen.exitonclick()
