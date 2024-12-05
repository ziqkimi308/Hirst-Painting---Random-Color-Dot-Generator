"""
********************************************************************************
* Project Name:  Hirst Painting - Random Color Dot Generator
* Description:   This project is inspired by the iconic spot paintings of Damien Hirst, blending art with Python programming
* Author:        ziqkimi308
* Created:       2024-12-05
* Updated:       2024-12-05
* Version:       1.0
********************************************************************************
"""

# Import
# import colorgram
import turtle
import random
from turtle import Screen

# Extract colors from image
# colors = colorgram.extract("image.jpg", 30)
# colors_list = []
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     rgb = (r, b, g)
#     colors_list.append(rgb)

# Main code

# Variable
color_list = [(202, 110, 164), (236, 243, 239), (149, 50, 75), (222, 136, 201), (53, 123, 93), (170, 41, 154), (138, 20, 31), (134, 184, 163), (197, 73, 92), (47, 86, 121), (73, 35, 43), (145, 149, 178), (14, 70, 98), (232, 165, 176), (160, 158, 142), (54, 50, 45), (101, 77, 75), (183, 171, 205), (36, 74, 60), (19, 89, 86), (82, 129, 148), (147, 19, 17), (27, 102, 68), (12, 64, 70), (107, 153, 127), (176, 208, 192), (168, 102, 99)]
tim = turtle.Turtle()
tim.speed("fastest")
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)


# Random color dot
turtle.colormode(255) # setup to use rgb
number_of_dots = 100
for i in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if i % 10 == 0: # Turtle execute this every 10 dots
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



# Screen Module
screen = turtle.Screen()
screen.exitonclick()

