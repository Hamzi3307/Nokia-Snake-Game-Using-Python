from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

my_scr = Screen()
my_scr.setup(width=600, height=600)
my_scr.bgcolor("black")
my_scr.title("Nokia Snake Game")
my_scr.tracer(0)

snake = Snake()
food = Food()
score = Score()


my_scr.listen()
my_scr.onkey(snake.up, "Up")
my_scr.onkey(snake.down, "Down")
my_scr.onkey(snake.right, "Right")
my_scr.onkey(snake.left, "Left")

game_on = True
while game_on:
    my_scr.update()
    time.sleep(0.1)
    snake.move()
    
    # Detect Collisions with Food
    if snake.segments[0].distance(food) < 20:
        food.refresh()
        # update score on collision with food
        score.increase_score()
        # add segment to snake
        snake.extend()
        
    # Detect Collisions with wall
    if snake.segments[0].xcor() < -280 or snake.segments[0].ycor() < -280 or snake.segments[0].xcor() > 280 or snake.segments[0].ycor() > 280:
            score.reset()
            snake.reset()
            food.refresh()
        
    # Detect Collision with Snake's Body
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            score.reset()
            snake.reset()
            food.refresh()

my_scr.exitonclick()