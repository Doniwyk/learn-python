from turtle import Turtle, Screen
import random


tim = Turtle()


def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b


def draw_shape(side_num):
    angle = 360 / side_num
    for j in range(side_num):
        tim.forward(100)
        tim.right(angle)
    side_num += 1


for i in range(3, 11):
    tim.color(random_color())
    draw_shape(i)

screen = Screen()
screen.exitonclick()
