from turtle import Screen, Turtle
import random

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turn off screen updates to improve performance

# Snake
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
snake = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    snake.append(new_segment)

head = snake[0]

# Food setup
food = Turtle("square")
food.color("red")
food.penup()
food.goto(random.randint(-280, 280), random.randint(-280, 280))

def move():
    for seg_num in range(len(snake) - 1, 0, -1):
        new_x = snake[seg_num - 1].xcor()
        new_y = snake[seg_num - 1].ycor()
        snake[seg_num].goto(new_x, new_y)
    head.forward(20)

def up():
    if head.heading() != 270:
        head.setheading(90)

def down():
    if head.heading() != 90:
        head.setheading(270)

def left():
    if head.heading() != 0:
        head.setheading(180)

def right():
    if head.heading() != 180:
        head.setheading(0)

screen.listen()
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    move()

    # Detect collision with food -->
    if head.distance(food) < 20:
        food.goto(random.randint(-280, 280), random.randint(-280, 280))
        # Add a new segment to the snake
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(snake[-1].xcor(), snake[-1].ycor())
        snake.append(new_segment)

    # Detect collision with wall or itself
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        game_is_on = False
    for segment in snake[1:]:
        if head.distance(segment) < 10:
            game_is_on = False

screen.exitonclick()