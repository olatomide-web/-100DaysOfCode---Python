#from turtle import Turtle, Screen
import turtle as t
import random


my_ijapa = t.Turtle()

t.colormode(255)

def random_colors():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

directions = [0, 90, 180, 270]
my_ijapa.pensize(10)
my_ijapa.speed("fastest")



for side in range(500):
    
    my_ijapa.color(random_colors())
    my_ijapa.forward(30)
    my_ijapa.setheading(random.choice(directions))

