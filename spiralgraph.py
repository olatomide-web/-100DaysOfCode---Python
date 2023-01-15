#from turtle import Turtle, Screen
import turtle as t
import random


my_ijapa = t.Turtle()

t.colormode(255)

def random_colors():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color


my_ijapa.speed("fastest")

def draw_spiral(size_of_gap):
    for loop in range(int(360 / size_of_gap)):
        my_ijapa.color(random_colors())
        my_ijapa.circle(100)
        my_ijapa.setheading(my_ijapa.heading() + size_of_gap)

draw_spiral(5)




screen = t.Screen()
screen.exitonclick()


