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


tim.speed("fastest")


def draw_spirograph(gap_size):
    for i in range(int(360 / gap_size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap_size)


draw_spirograph(10)
screen = Screen()
screen.exitonclick()
