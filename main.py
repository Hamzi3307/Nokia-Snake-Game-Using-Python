from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Nokia Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on = True
while game_on:
    screen.update()
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

screen.exitonclick()