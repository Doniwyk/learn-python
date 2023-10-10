from turtle import Turtle, Screen
import random

tim = Turtle()


def random_direction():
    turn = [0, 90, 180, 270]
    return random.choice(turn)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"#{r:02X}{g:02X}{b:02X}"


for i in range(200):
    tim.pensize(10)
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random_direction())

screen = Screen()
screen.exitonclick()
