# import colorgram

# rgb_colors = []
# colors = colorgram.extract('img/image.jpeg', 6)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

import random
import turtle as t

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.ht()
color_list = [(14, 27, 34), (162, 155, 148), (84, 96, 91), (63, 79, 84), (117, 114, 107), (218, 213, 210)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_dots = 100

for i in range(1, num_dots + 1):
    tim.dot(20, "#{:02X}{:02X}{:02X}".format(*random.choice(color_list)))
    tim.forward(50)

    if i % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
