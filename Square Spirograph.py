from turtle import *
import turtle
speed(0)
bgcolor("black")
pensize(3)
for x in range (5):
    for colors in ["red","pink","blue","cyan","green","yellow","white"]:
        color(colors)
        left(12)
        for i in range(4):
            forward(200)
            left(90)
turtle.done()