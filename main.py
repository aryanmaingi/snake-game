import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("my snake game ")
screen.tracer(0)
i = 0

snake = Snake()
food = Food()
score = Score()
type = int(screen.numinput("DIFFICULTY","Enter: ", minval=1, maxval=3))
speed = [0.1, 0.05, 0.025]

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game = True
while game:
    screen.update()
    time.sleep(speed[type-1])
    snake.move()

    # detect food collision
    if snake.head.distance(food) < 20:
        food.refresh()
        score.sc += 1
        score.score_cr()
        snake.extend()

    # detect wall collision
    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.game_over()
        game = False

    for seg in snake.segments[1::]:
        if snake.head.distance(seg) < 10:
            score.game_over()
            game = False

screen.exitonclick()